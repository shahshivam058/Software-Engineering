# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class PublicClass:
    # Public attribute - accessible from anywhere
    public_attr = 20
    
    # Protected attribute (convention) - meant for internal use and subclass access
    _protected_attr = 30
    
    # Private attribute (name mangling) - intended only for use within this class
    __private_attr = 40
    
    def __init__(self, value):
        self.instance_public = value
        self._instance_protected = value + 10
        self.__instance_private = value + 20
    
    # Public method
    def public_method(self):
        return f"Public: {self.public_attr}, {self.instance_public}"
    
    # Protected method
    def _protected_method(self):
        return f"Protected: {self._protected_attr}, {self._instance_protected}"
    
    # Private method
    def __private_method(self):
        return f"Private: {self.__private_attr}, {self.__instance_private}"
    
    # Method to access private members (common pattern)
    def access_private(self):
        return self.__private_method()


# Subclass to demonstrate protected access
class SubClass(PublicClass):
    def __init__(self, value):
        super().__init__(value)
    
    def access_protected(self):
        # Can access protected attributes from parent class
        return f"Subclass accessing protected: {self._protected_attr}, {self._instance_protected}"
    
    def try_access_private(self):
        # Cannot directly access private attributes from parent class
        try:
            return self.__private_attr
        except AttributeError:
            return "Cannot access private attribute from subclass"


# Create instances and demonstrate access
if __name__ == "__main__":
    # Create instance
    obj = PublicClass(100)
    
    print("=== Direct Access ===")
    # Public access - works everywhere
    print("Public attribute:", obj.public_attr)
    print("Public method:", obj.public_method())
    
    # Protected access - works but against convention
    print("Protected attribute (direct access):", obj._protected_attr)
    print("Protected method (direct access):", obj._protected_method())
    
    # Private access - name mangling makes it harder but not impossible
    print("Private attribute (via name mangling):", obj._PublicClass__private_attr)
    print("Private method (via name mangling):", obj._PublicClass__private_method())
    
    # Access private through public method
    print("Private access via public method:", obj.access_private())
    
    print("\n=== Subclass Access ===")
    sub_obj = SubClass(200)
    print("Subclass public access:", sub_obj.public_method())
    print(sub_obj.access_protected())
    print(sub_obj.try_access_private())
    
    print("\n=== Access from Outside ===")
    # Even private attributes can be accessed with name mangling
    print("Instance private (outside):", sub_obj._PublicClass__instance_private)