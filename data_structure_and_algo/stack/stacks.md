Stack :

- An Abstract Data Type (ADT) is a mathematical model for a data type that is defined by its behavior, a set of values, and a set of operations on that data. It's a conceptual blueprint that tells you what a data type does, not how it does it. This separation of concerns allows you to define the functionality of a data type without getting bogged down in implementation details.

- Abstract Data Type (ADT): The logical model or the "what." It's a high-level description of a data type and its operations. For example, a Stack ADT defines operations like push(), pop(), and peek(), but it doesn't specify whether it's built using an array or a linked list. The user of a Stack ADT only needs to know about these operations, not the underlying code.

- A stack is an abstract data type that stores a collection of elements. Think of it like a stack of plates: you can only add a new plate to the top, and you can only take a plate from the top. This is known as the Last-In, First-Out (LIFO) principle. The last element you added is the first one you can remove.


Core Operations
There are two primary operations on a stack:

    - Push: Adds an element to the top of the stack.
    - Pop: Removes and returns the top element of the stack.

You can also perform other operations, such as:

    - Peek or Top: Returns the top element without removing it.
    - IsEmpty: Checks if the stack is empty.
    - Size: Returns the number of elements in the stack.

Array-based Implementation
- An array-based stack uses a dynamic array to store elements. You also need a variable, let's call it top, to keep track of the index of the top element.
-Push: To push an element, you increment the top index and place the new element at array[top]. If the array is full, you might need to resize it by creating a new, larger array and copying the elements. This can be an O(N) operation in the worst case, but amortized to O(1).
-Pop: To pop an element, you retrieve the element at array[top] and then decrement the top index. This is an O(1) operation.


Pros:

- Faster access to elements since they are stored contiguously in memory.
- Simple to implement.

Cons:

- Fixed size (unless you use a dynamic array), which can lead to overflow if you try to push too many elements.
- Resizing can be an expensive operation.


Time Complexity
The efficiency of a list-based stack hinges on the performance of its core operations.

- Push (append): This operation has an amortized time complexity of O(1). While most appends are constant time, a list is a dynamic array, meaning that if it runs out of space, it must allocate a new, larger block of memory and copy all existing elements over. This worst-case scenario is an O(N) operation, but since it happens infrequently and the list size grows exponentially, the average time over many operations is still constant.

- Pop (pop()): Popping the last element from a list is a constant time operation, O(1), because you don't need to shift any other elements. You're simply removing the item at the end.

- Peek: Accessing the last element by index is also a constant time operation, O(1).



Linked List-based Implementation
- A linked list-based stack uses a singly linked list. You maintain a pointer, usually called head or top, that points to the first node of the list.
- Push: To push an element, you create a new node, set its next pointer to the current top node, and then update the top pointer to the new node. This is an O(1) operation.
- Pop: To pop an element, you retrieve the value of the top node, then update the top pointer to the next node in the list. This is also an O(1) operation.

Pros:

- Dynamic size; you never have to worry about overflow as long as there is enough memory.
- No need for resizing.

Cons:

- Slightly more memory overhead due to storing pointers for each node.


- Function Call Stack: This is one of the most important applications. When a program calls a function, its parameters and local variables are pushed onto the call stack. When the function returns, its information is popped off. This manages the flow of control and memory allocation.

- Expression Evaluation: Used to convert infix expressions (e.g., 2 + 3 * 4) to postfix (e.g., 2 3 4 * +) and then evaluate them.

- Undo/Redo Functionality: Most software applications use a stack to implement undo/redo. Every action a user performs is pushed onto a stack. To undo, you pop the last action. To redo, you pop from the undo stack and push onto the redo stack.

- Browser History: The back button in a web browser is implemented using a stack. Every time you visit a new page, its URL is pushed onto the stack. When you hit the "back" button, the last URL is popped, and you go to the previous page.

- Depth-First Search (DFS): In graph and tree traversal algorithms, a stack is often used to keep track of the nodes to visit next.

Monotonic stack : 

- A monotonic stack is a specialized stack data structure where the elements are always kept in a strict order—either monotonically increasing or monotonically decreasing. This property is maintained by a clever push and pop logic, which makes it incredibly efficient for solving a class of problems that would otherwise require much slower brute-force methods. The core idea is that the stack only holds elements that could potentially be a "next greater/smaller element" for future elements in a sequence, discarding irrelevant ones on the fly.

- A stack is monotonically increasing if its elements are always in ascending order from the bottom to the top. Conversely, a stack is monotonically decreasing if its elements are always in descending order. The term "monotonic" means the values are non-decreasing (increasing or staying the same) or non-increasing (decreasing or staying the same), depending on the problem.

- For a Monotonically Increasing Stack: If the new element is smaller than the stack's top, it "invalidates" the top element (and possibly others below it) as a candidate for the next smaller element. You pop elements from the stack's top as long as they are greater than the current element. Then, you push the new element onto the stack. This process ensures the stack remains sorted.


- For a Monotonically Decreasing Stack: If the new element is larger than the stack's top, it "invalidates" the elements at the top as a candidate for the next greater element. You pop elements from the stack's top as long as they are smaller than the current element. Then, you push the new element onto the stack.


- Monotonic stacks are used to solve problems that involve finding the "next greater/smaller element" or "previous greater/smaller element" for each element in an array. A common brute-force approach for these problems would involve nested loops, leading to an O(n ** 2) time complexity. A monotonic stack, however, can solve them in linear time, O(n). This is because each element from the input sequence is pushed onto and popped from the stack at most once, making the overall operations incredibly efficient.

Queue :

- A queue is a fundamental and widely used linear data structure that adheres to the First-In, First-Out (FIFO) principle. This means the first element added to the queue is the first one to be removed. It's a perfect analogy for a real-world line or queue of people waiting for a service—the person who has been in line the longest is the next to be served.

A queue is defined by two primary operations that dictate its behavior:

    - Enqueue: This operation adds an element to the rear (or tail) of the queue.
    - Dequeue: This operation removes and returns the element from the front (or head) of the queue.

In addition to these, a queue typically supports other operations:

    - Peek or Front: Returns the element at the front of the queue without removing it.
    - IsEmpty: Checks if the queue contains any elements.
    - Size: Returns the number of elements currently in the queue.

Array-based Implementation :
    An array-based queue uses a fixed-size array and two pointers or indices: front and rear.
        - front: Points to the first element of the queue.
        - rear: Points to the last element of the queue.
    
    How it works:
        - Enqueue: An element is added to array[rear], and then rear is incremented.
        - Dequeue: The element at array[front] is removed, and then front is incremented.
    

    A key issue with a simple array implementation is that front and rear keep moving forward, potentially wasting space at the beginning of the array. To solve this, a circular array implementation is used. In this approach, when an index reaches the end of the array, it wraps around to the beginning, using the modulo operator (%).


    Time Complexity:

        Enqueue: O(1) - Adding an element at the rear is a constant-time operation.
        Dequeue: O(1) - Removing an element from the front is a constant-time operation.

    Pros:

        Space efficiency, especially with circular arrays, as there's no overhead for pointers.
        Simple to implement for a fixed-size queue.

    Cons:

        Fixed size; the queue can become full.
        Can be tricky to manage front and rear pointers, especially in a circular array.


Linked List-based Implementation :

- A linked list-based queue uses a singly linked list. To make both enqueue and dequeue operations efficient, two pointers are maintained: front and rear, pointing to the first and last nodes of the list, respectively.


How it works:

    - Enqueue: A new node is created and added to the end of the list by updating the rear pointer and the next pointer of the previous rear node.
    - Dequeue: The front pointer is moved to the next node in the list, and the old front node is removed.

Time Complexity:

    - Enqueue: O(1) - Adding a node at the tail is a constant-time operation.
    - Dequeue: O(1) - Removing a node from the head is a constant-time operation.

Pros:

    - Dynamic size; the queue can grow or shrink as needed, preventing overflow.
    - No need for resizing or complex pointer management like in circular arrays.

Cons:

    - Requires more memory due to the overhead of storing pointers in each node.


Circular Array :


- A circular queue is a linear data structure that operates on the First-In, First-Out (FIFO) principle, similar to a regular queue. However, it's implemented using a fixed-size array in a way that the end of the array is connected to the beginning. This allows for efficient reuse of empty space and helps overcome a major limitation of a simple array-based queue.

- In a basic array-based queue, when you dequeue an element, the front index moves forward. Over time, the space at the beginning of the array becomes empty, but it cannot be reused because the rear index is still moving towards the end. This leads to a scenario where the queue is considered "full" even if there's available space at the front. A circular queue solves this problem by conceptually wrapping the array around.


Core Operations and Logic

A circular queue uses a fixed-size array and two pointers, front and rear, to manage the elements.

- front: Points to the index of the first element in the queue.
- rear: Points to the index where the next element will be inserted.
- The key to its circular behavior is the use of the modulo operator (%) to manage index movement.




1. Enqueue (Adding an Element)
- To add an element to the circular queue, you check if the queue is full.
- Condition for Full Queue: The queue is full when the next position for rear is equal to front. This is calculated as (rear + 1) % capacity == front.
- Process: If the queue is not full, you place the new element at the rear index and then update rear using the modulo operator: rear = (rear + 1) % capacity.



2. Dequeue (Removing an Element)
- To remove an element from the circular queue, you check if the queue is empty.
- Condition for Empty Queue: The queue is empty when front is equal to rear.
- Process: If the queue is not empty, you retrieve the element at the front index. Then, you update front using the modulo operator: front = (front + 1) % capacity.

3. Other Operations
- Peek: Returns the element at the front index without removing it. This operation also requires a check to ensure the queue is not empty.
- IsEmpty: Returns true if front == rear, indicating the queue is empty.
- IsFull: Returns true if (rear + 1) % capacity == front, indicating the queue is full.



Advantages and Disadvantages
Advantages
- Efficient Space Utilization: Unlike a simple array queue, a circular queue reuses the empty slots at the beginning of the array, preventing a situation where the queue is declared full prematurely.
- Constant Time Operations: Both enqueue and dequeue operations are O(1), which is highly efficient.

Disadvantages
- Fixed Size: A circular queue is still implemented on a fixed-size array, meaning it can overflow if you try to add more elements than its capacity.
- Slightly More Complex Logic: The use of the modulo operator and the special conditions for isFull and isEmpty can make the implementation slightly more complex than a linked list-based queue.




The Ambiguity: front == rear
The fundamental challenge with a circular queue is that both a full and an empty queue can have the front and rear pointers pointing to the same location.

- Empty Queue: When the queue is initialized, front and rear are often set to the same value (e.g., -1 or 0) to indicate that there are no elements. After all elements are dequeued, the pointers return to this same state.
- Full Queue: When the queue becomes full after several enqueue and dequeue operations, the rear pointer will have wrapped around and will be positioned right before the front pointer, making them point to the same location on the array.

Double Ended Queue : 

- A Double-Ended Queue (Deque), pronounced "deck," is a generalized form of a queue where elements can be added or removed from both the front and the rear. It's a versatile data structure that combines the functionalities of both a queue (FIFO) and a stack (LIFO).

A Deque provides four primary operations, allowing flexibility in how you manipulate the data:

- addFront (or pushFront): Adds an element to the front of the deque.
- addRear (or pushRear): Adds an element to the rear of the deque.
- removeFront (or popFront): Removes and returns the element from the front.
- removeRear (or popRear): Removes and returns the element from the rear.
- peekFront: Returns the element at the front without removing it.
- peekRear: Returns the element at the rear without removing it.
- isEmpty: Checks if the deque is empty.



1. Doubly Linked List-based Implementation
- This is often the preferred and most intuitive way to implement a Deque. A doubly linked list has nodes that contain a value and two pointers: one to the next node and one to the previous node. You maintain pointers to both the head and the tail of the list.
- addFront: A new node is created and made the new head. Its next pointer points to the old head, and the old head's prev pointer is updated to point to the new node.
- addRear: A new node is added after the tail. The old tail's next pointer is updated to the new node, and the new node's prev pointer points to the old tail. The new node then becomes the new tail.
- removeFront: The head is moved to its next node. The old head is then removed.
- removeRear: The tail is moved to its prev node. The old tail is then removed.
- Time Complexity: All four primary operations (addFront, addRear, removeFront, removeRear) are O(1).

2. Dynamic Array-based Implementation
- A dynamic array can be used, but it's more complex to implement efficiently. Adding/removing elements from the rear is straightforward (append/pop), but adding/removing from the front can be costly as it requires shifting all other elements.

- To achieve O(1) time complexity for front operations, a circular array implementation is used, similar to a circular queue. You maintain front and rear pointers and use the modulo operator (%) to handle wraparound. This approach can be tricky to manage.

Time Complexity:

- addRear & removeRear: Amortized O(1).
- addFront & removeFront: Amortized O(1) (if implemented with a circular array).

Pros:

- Better cache locality due to contiguous memory allocation.
- Lower memory overhead compared to a linked list.

Cons:

- Can involve expensive O(n) resizing operations in the worst case if not managed carefully.
- More complex to implement correctly than a linked list.

