
- A linked list is one of the most fundamental and flexible linear data structures used in computer science. It provides an efficient alternative to arrays for situations where the number of elements changes frequently and insertion/deletion operations are common.

- Unlike an array, which stores elements in contiguous memory locations, a linked list stores elements in separate, non-contiguous blocks of memory called nodes. The "link" between the elements is achieved through pointers.

- The Node
    - The basic building block of a linked list is the node. Each node typically consists of two main parts:
    - Data Field: Stores the actual value or information.
    - Pointer (or Next) Field: Stores the memory address (a reference) of the next node in the sequence.

- Head Pointer: The linked list is accessed only through a special pointer called the Head. The Head stores the memory address of the first node in the list. If the Head is NULL, the list is empty.
- Tail Node: The last node's pointer field is set to NULL (or Λ), signifying the end of the list.


- Need Of Linked list
    - Dynamic Memory Allocation : 
        - Arrays have a fixed size; once declared, the size cannot be changed easily.
        - A linked list can grow or shrink at runtime since memory is allocated for each node dynamically
    
    - Efficient Insertions/Deletions
        - In arrays, inserting or deleting an element in the middle requires shifting elements, which is costly (O(n)).
        - In linked lists, insertion and deletion can be done in O(1) time if the pointer to the node is known, because only the links need to be updated.

    - No Wasted Memory
        - In arrays, you might allocate extra space “just in case,” which wastes memory, or run out of space if underestimated.
        - Linked lists allocate memory node by node, avoiding unused memory.

    - Implementation of Advanced Data Structures
        - Linked lists are the building blocks for stacks, queues, graphs, hash tables, and adjacency lists.

    - Flexibility in Data Organization
        - Variants like doubly linked lists (nodes link to both previous and next) and circular linked lists provide flexibility for implementing complex structures such as navigation systems, playlist rotations, and memory management.



- Multiple ADT can be implemented using Linked List :
    - Stack
    - Queue
    - Tree
    - Graph

- Memory Management: Operating systems use linked lists (specifically, Doubly Linked Lists) to manage free and allocated blocks of memory (memory partitioning algorithms).

- File Systems: Used in some file allocation methods (like the linked allocation scheme) where file blocks are stored non-contiguously, and a list of pointers links them together.

- Process/Job Scheduling: The OS maintains lists of processes waiting for the CPU or I/O devices.

Single Linked List :

- A Single Linked List (or Singly Linked List) is a fundamental, linear data structure where elements are not stored at contiguous memory locations. Instead, elements are linked to one another using pointers or references.

- A single linked list is composed of a sequence of elements called nodes.

    -The Node
        - Each node in a single linked list typically consists of two main parts:

    - Data (or Payload): 
        - This holds the actual information or value that the element represents. The data type can be anything (integer, string, object, etc.).

    - Next Pointer (or Link): 
        - This is a reference or memory address that points to the next node in the sequence. It's how the elements are logically linked together. The last node's pointer is typically set to NULL (or nil) to signify the end of the list.

The List Head
    - The entire linked list is accessed through a special pointer called the Head (or Start).
    - Head: This is a pointer that points to the first node in the list.
    - If the list is empty, the Head pointer is set to NULL.

Linear Structure        : The elements are arranged in a sequential, linear order.
Dynamic Size	        : Linked lists can easily grow or shrink in size during execution. Memory is allocated only when a node is added.
Non-Contiguous Memory	: Nodes are typically scattered throughout memory. The 'next' pointers provide the logical ordering.
Directionality          : Traversal can only occur in one direction (forward), from the head to the tail, because each node only holds a pointer to the next node.



- Traversal
    - Start at head and follow next until NULL.
    - Time Complexity → O(n).


There are multiple cases:

Insert at Beginning (Head Insertion)
    - Create new node.
    - New node’s next = current head.
    - Update head to new node.
    - TC : O(1).

Insert at End (Tail Insertion)
    - Traverse to last node.
    - Last node’s next = new node.
    - O(n) (unless tail pointer maintained → O(1)).

Insert at Specific Position
    - Traverse to node before position.
    - Adjust pointers.
    - TC :O(n).

Delete at Beginning
    - Move head to head.next.
    - Free old node.
    - TC : O(1).

Delete at End
    - Traverse to second last node.
    - Set its next = NULL.
    - Free last node.
    - TC : O(n).

Delete at Specific Position
    - Traverse to node before target.
    - Adjust pointers.
    - TC : O(n).

- Search
    - Traverse until data is found or end reached.
    - TC : O(n).

Doubly Linked List :

- A Doubly Linked List is a fundamental type of linked data structure that consists of a set of sequentially linked elements called nodes. Unlike a Single Linked List, a doubly linked list allows for bidirectional traversal because each node contains pointers to both the next node and the previous node in the sequence.

Node : 
    - Each node in a doubly linked list is composed of three main parts:
    - Data (or Payload): Holds the actual value or information stored in the node.
    - Next Pointer (Forward Link): A reference or memory address that points to the next node in the sequence. For the last node (the Tail), this pointer is set to NULL (nil).
    - Prev Pointer (Backward Link): A reference or memory address that points to the previous node in the sequence. For the first node (the Head), this pointer is set to NULL (nil).


- Head (or Start): A pointer that always points to the first node of the list.
- Tail (or End): A pointer that always points to the last node of the list.

Bidirectional Traversal	 : The list can be traversed from the Head to the Tail (using the Next pointers) or from the Tail to the Head (using the Prev pointers).
Dynamic Size	         : Similar to a single linked list, it can easily grow or shrink as needed during execution.
Non-Contiguous Memory    : Nodes are typically scattered in memory; the pointers maintain the logical order.
Increased Overhead       : Each node requires two pointer fields (Prev and Next), consuming more memory than a single linked list node.

Traversal
    - Forward traversal: start from head, follow next.
    - Backward traversal: start from tail, follow prev.
    - Time Complexity → O(n).

Insert at Beginning
    - Create new node.
    - Set new.next = head.
    - Set head.prev = new.
    - Update head = new.
    - TC : O(1).

Insert at End
    - Traverse to tail.
    - tail.next = new.
    - new.prev = tail.
    - O(n) (O(1) if tail pointer maintained).

Insert at Position
    - Traverse to target position.
    - Adjust both next and prev pointers of surrounding nodes.
    - TC : O(n).

Delete at Beginning
    - Move head → head.next.
    - Set head.prev = NULL.
    - O(1).

Delete at End
    - Move tail → tail.prev.
    - Set tail.next = NULL.
    - O(n) (O(1) with tail pointer).

Delete at Position
    - Adjust both neighbors’ pointers.
    - TC : O(n).


Search
    - Traverse forward or backward until element is found.
    - O(n).

Circular Linked List :

- A Circular Linked List (CLL) is a variation of a traditional linked list where the last node in the sequence points back to the first node, forming a continuous, closed loop. Unlike Singly or Doubly Linked Lists, a CLL has no NULL pointer to mark the end of the list, allowing for perpetual traversal.

- The Node
    - The basic building block of a linked list is the node. Each node typically consists of two main parts:
    - Data Field: Stores the actual value or information.
    - Pointer (or Next) Field: Stores the memory address (a reference) of the next node in the sequence.

- The Linkage: The Crucial Difference
    - The circular structure is defined by the connection between the tail and the head:
    - In a Single Linked List, the last node's next pointer is NULL.
    - In a Circular Linked List, the last node's next pointer points to the Head (first node).


- Traversal
    - Start from head.
    - Keep moving using next pointer.
    - Stop when you come back to head.
    - Time Complexity → O(n).


Insert at Beginning
    - Create a new node.
    - New node’s next = head.
    - Update last node’s next → new node.
    - Update head = new.
    - TC : O(n) (need to reach last node).

Insert at End

    - Create a new node.
    - Last node’s next = new.
    - New node’s next = head.
    - TC :O(n).

Insert at Position
    - Traverse to target position.
    - Adjust next pointers.
    - TC : O(n).


Delete at Beginning

    - Find last node.
    - Last node’s next = head.next.
    - Move head = head.next.
    - O(n).

Delete at End

    - Traverse to second last node.
    - Set its next = head.
    -  O(n).

Delete at Position
    - Traverse to node before target.
    - Adjust next.
    - TC : O(n).

Search
    - Traverse until element is found or back to head.
    - TC : O(n).