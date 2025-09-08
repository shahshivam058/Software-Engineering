def create_array():
    arr = [0] * 10
    count = 0

    for index in range(len(arr)):
        arr[index] = count
        count += 1
    
    return arr

arr = create_array()
for num in arr : 
    print(num)


"""
What is a Data Structure?
A data structure is a way of organizing and storing data in a computer so it can be accessed, modified, and processed efficiently.

It defines:

How data is stored in memory (RAM, disk, etc.).
How data elements relate to each other (e.g., sequentially, hierarchically, linked).
What operations can be performed efficiently (insert, search, delete, etc.).

Examples: Array, Linked List, Stack, Queue, Tree, Graph, Hash Table.

Data Representation in Memory (RAM)
RAM is the primary working memory of a computer.Data is stored in binary form (0s and 1s), and the processor uses it directly.

1. Bit & Byte
    Bit: The smallest unit of storage; can store 0 or 1.
    Byte: 8 bits. Most CPUs read/write memory in bytes (or multiples of bytes).

2. RAM Organization
    RAM can be 2 GB, 4 GB, 8 GB, 16 GB, 32 GB, etc. (always a power of 2).
    It is divided into memory cells.

Each cell has:
    Address: A unique number (like a house number) identifying the location.
    Value: The actual data stored there (in binary form).

3. Address Size
    The number of bytes used to store an address depends on CPU architecture:
    32-bit CPU → Address is 4 bytes (can access up to 4 GB directly).
    64-bit CPU → Address is 8 bytes (much larger addressable memory).
    Each address points to 1 byte of memory.

4. Storing Data
    The way data is stored depends on its type:
    Integer (4 bytes on many systems) → occupies 4 consecutive addresses.
    Character (1 byte) → occupies 1 address.
    Double (8 bytes) → occupies 8 consecutive addresses.

The compiler decides how many bytes a type needs and aligns them properly in memory.


A static array is a fixed-size data structure that stores a collection of elements of the same data type in contiguous memory locations. 
It's one of the simplest and most fundamental data structures in computer science. Once a static array is created, its size cannot be changed. 
This means you must know the exact number of elements you'll need to store at the time of creation.

Array can be also used to refrance collection of element using single veriable 

Key Characteristics
Fixed Size: The size of a static array is determined at compile time or at the time of its declaration. 
            You cannot add or remove elements beyond this initial capacity.

Homogeneous Data: All elements in a static array must be of the same type. For example, you can have an array of integers (int), 
                an array of characters (char), or an array of floating-point numbers (float), but you cannot mix these types within the same array.

Contiguous Memory Allocation: The elements of a static array are stored one after the other in a single, unbroken block of memory. 
                  This is a crucial feature that allows for very efficient access to elements.

Zero-Based Indexing: In most programming languages, the elements of an array are accessed using an index, which starts at 0 and goes up to n−1, 
                    where n is the total number of elements. The first element is at index 0, the second at index 1, and so on.





How Static Arrays Work

When you declare a static array, the compiler reserves a specific amount of memory for it. 
Because the size is fixed and all elements are of the same type, the compiler knows exactly how much memory to allocate.

To access a specific element, the computer uses a simple formula:

addresselement​ = baseaddress​ + (index × sizeofelement​​)
baseaddress​ is the memory address of the first element (index 0).
index is the position of the element you want to access.
sizeofelement​​ is the size in bytes of a single element (e.g., 4 bytes for an integer on a 32-bit system).



✅ Advantages
Fast Access: Due to contiguous memory allocation and direct indexing, accessing any element is extremely fast (O(1)).
Memory Efficiency: There is no overhead for managing the size of the array, making it memory efficient.
Simplicity: It is a straightforward data structure to understand and implement.

❌ Disadvantages
Fixed Size: This is the biggest limitation. You can't resize an array if you need to store more elements than initially planned. This can lead to wasted memory if you allocate a large array that isn't fully used, or an overflow error if you try to store too many items.
Inefficient Insertion/Deletion: Inserting an element into or deleting an element from the middle of a static array requires shifting all subsequent elements, which can be a slow process (O(n)).
No Dynamic Resizing: To "resize" a static array, you would have to create a new, larger array and copy all the elements from the old array to the new one, which is a very expensive operation.

Memory Locations
Arrays can be stored in different parts of a computer's memory, depending on how they're declared:
Stack: Arrays declared inside a function (local arrays) are typically allocated on the stack. The stack is a fast, but limited memory area.
Heap: Arrays allocated dynamically at runtime (using functions like malloc in C or new in C++) are stored on the heap. The heap is a larger, more flexible memory area, but it's slower to access than the stack.
Data Segment: Global or static arrays are stored in a part of memory called the data segment, which exists for the entire duration of the program.



A dynamic array is a data structure that, unlike a static array, can grow or shrink in size at runtime. It's built on top of a static array, 
using it as an underlying storage mechanism. When a dynamic array runs out of space, it automatically handles the process of resizing to accommodate 
new elements. This flexibility makes it a very popular and useful data structure in many programming languages. 📈

Key Characteristics
Variable Size: A dynamic array's capacity can change during program execution. You don't have to know its final size when you create it.
Contiguous Memory: Like static arrays, elements are stored in a single, continuous block of memory. This is crucial for its efficient access times.
Automatic Resizing: The core feature of a dynamic array is its ability to automatically resize itself when it reaches its capacity limit.
Amortized O(1) Insertion: While a single insertion might take O(n) time (if a resize is needed), the average or amortized time for an insertion is O(1). 
                          This is because resizes are infrequent.

How Dynamic Arrays Work
A dynamic array typically maintains three pieces of information:
    A pointer to the underlying static array: This points to the start of the memory block where the elements are actually stored.
    Size: The number of elements currently in the array.
    Capacity: The total number of elements the underlying static array can hold.
    


1. Access Operations
Access by Index
    Operation: arr[i]
    Time Complexity: O(1)
    Arrays provide direct access to elements using their index since elements are stored in contiguous memory locations.

2. Search Operations
Linear Search (Unsorted Array)
    Operation: Finding an element by value
    Time Complexity: O(n)
    Must check each element sequentially in worst case

Binary Search (Sorted Array)
    Operation: Finding an element in sorted array
    Time Complexity: O(log n)
    Eliminates half of remaining elements with each comparison

3. Insertion Operations
Insert at End
    Time Complexity: O(1) amortized
    Simply place element at the next available position
    May be O(n) if array needs resizing (dynamic arrays)

Insert at Beginning
    Time Complexity: O(n)
    Requires shifting all existing elements one position right

Insert at Specific Position
    Time Complexity: O(n)
    Requires shifting elements from that position onwards

4. Deletion Operations

Delete from End
    Time Complexity: O(1)
    Simply remove the last element

Delete from Beginning
    Time Complexity: O(n)
    Requires shifting all remaining elements one position left

Delete from Specific Position
    Time Complexity: O(n)
    Requires shifting elements after the deleted position

Delete by Value
    Time Complexity: O(n)
    Must first search for the element (O(n)), then delete it



"""
