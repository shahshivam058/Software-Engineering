import copy
from abc import ABC, abstractmethod
from typing import Any, Dict

class Prototype(ABC):
    """Abstract base class for prototype objects"""
    
    @abstractmethod
    def clone(self):
        """Clone the object"""
        pass

class Document(Prototype):
    """A document class that can be cloned"""
    
    def __init__(self, title: str, content: str, images: Dict[str, Any] = None):
        self.title = title
        self.content = content
        # Images is a dictionary representing embedded images
        self.images = images if images else {}
        # Simulate expensive initialization
        print(f"Creating a new document '{title}' (expensive operation)")
    
    def clone(self):
        """Create a deep copy of the document"""
        # Using deepcopy to ensure all nested objects are also copied
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Document(title='{self.title}', content='{self.content[:50]}...', images={list(self.images.keys())})"

# Client code
if __name__ == "__main__":
    # Create a prototype document with complex initialization
    original_doc = Document(
        title="Annual Report",
        content="This is the content of our annual report...",
        images={"chart1": "chart_data", "logo": "logo_data"}
    )
    
    print(f"Original: {original_doc}")
    
    # Clone the document instead of creating a new one from scratch
    cloned_doc = original_doc.clone()
    cloned_doc.title = "Annual Report - Copy"
    
    print(f"Clone: {cloned_doc}")
    
    # Demonstrate that they are different objects
    print(f"Are they the same object? {original_doc is cloned_doc}")
    print(f"Same title? {original_doc.title == cloned_doc.title}")
    
    # Modify the clone's content to show independence
    cloned_doc.content = "Modified content for the cloned document..."
    print(f"After modification - Original content: {original_doc.content[:30]}...")
    print(f"After modification - Clone content: {cloned_doc.content[:30]}...")
    
    # Demonstrate deep copy with nested objects
    cloned_doc.images["new_chart"] = "new_data"
    print(f"Original images: {list(original_doc.images.keys())}")
    print(f"Clone images: {list(cloned_doc.images.keys())}")





import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Document(Prototype):
    def __init__(self, title, content, images=None, styles=None):
        self.title = title
        self.content = content
        self.images = images or []
        self.styles = styles or {}
        print(f"Initializing document '{title}'")
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Document('{self.title}')"

class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}
    
    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype
    
    def clone(self, name, **attrs):
        obj = self._prototypes[name].clone()
        for key, value in attrs.items():
            setattr(obj, key, value)
        return obj

# Usage
if __name__ == "__main__":
    registry = PrototypeRegistry()
    
    # Register prototypes
    registry.register_prototype(
        "basic_doc",
        Document("Basic Document", "Content", [], {})
    )
    
    # Create new documents
    doc1 = registry.clone("basic_doc", title="Doc 1", content="Content 1")
    doc2 = registry.clone("basic_doc", title="Doc 2", content="Content 2")
    
    print(doc1)
    print(doc2)