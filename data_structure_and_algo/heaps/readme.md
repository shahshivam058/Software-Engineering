- A Heap is a specialized tree-based data structure that satisfies the Heap Property:
    - In a Max Heap, for every node i, the value of i is greater than or equal to the values of its children.
    - In a Min Heap, for every node i, the value of i is less than or equal to the values of its children.

- Complete Binary Tree
    - A complete binary tree is a type of binary tree with a specific structure. It's defined by two key properties:
    - Every level of the tree, except possibly the last, is completely filled.
    - All nodes in the last level are as far left as possible.
    - This means that if you were to fill the tree level by level, from the root down, you would fill all the nodes from left to right without any gaps until you reach the end of the tree. A perfect binary tree is a special case of a complete binary tree where the last level is also completely filled.


- Heap Property
    - Maintains the ordering rule (max or min).
    - No requirement for ordering between siblings (not a Binary Search Tree!).

- Max-Heap Property: 
    For any given node, its value is greater than or equal to the values of its children. This means the largest element is always at the root of the tree.

- Min-Heap Property: 
    For any given node, its value is less than or equal to the values of its children. The smallest element is therefore always at the root.

- One of the most efficient ways to implement a heap is using an array. The "almost complete binary tree" structure allows for this compact representation. The relationships between parent and child nodes can be calculated using simple arithmetic:
    - The root of the tree is at index 0.
    - For a node at index i:
    - Its left child is at index 2i + 1.
    - Its right child is at index 2i + 2.
    - Its parent is at index (i - 1) / 2 (integer division).
    - This array representation is what makes heaps so space-efficient, as you don't need to store any pointers.


- The left-to-right traversal is about the physical shape of the tree. It ensures the tree is compact and can be stored efficiently in an array.


- we can rearrange array such that it may follow :
    - Max-Heap Property
    - Min-Heap Property

- we can also perform
    - Insert / Delete Max Heaps 
    - Insert / Delete Min Heaps 

Converting array To Min Heap : 0(n) ACTUALLY ITS O(nlogn)
Converting array To Max Heap : 0(n) ACTUALLY ITS O(nlogn)


- Heapify-Up :
    - Heapify-up is used after a new element has been inserted into the heap.
    - When you insert a new element, it is first placed in the next available spot at the end of the heap array (or, conceptually, at the next available leaf position in the tree). This is done to maintain the complete binary tree property. However, this new element might violate the heap property, for example, a larger value being placed under a smaller parent in a max-heap.


    - Start at the new node: Begin with the newly inserted element.
    - Compare with parent: Compare the element with its parent.
    - Swap if necessary:
        - In a max-heap, if the element's value is greater than its parent's, swap them.
        - In a min-heap, if the element's value is less than its parent's, swap them.
    - Repeat: After the swap, the element is now at a new position. Repeat the comparison and swapping process with its new parent.
    - Stop condition: The process stops when one of two conditions is met:
    - The element reaches the root of the tree.
    - The element is no longer violating the heap property (i.e., it is in the correct position relative to its parent).
    - Since the element moves up one level at a time and the height of a complete binary tree with n nodes is O(logn), the time complexity of a heapify-up operation is O(logn).

- Heapify-Down :
    - Heapify-down is used after an element, typically the root, has been removed or its value has been changed.
    - The most common use of heapify-down is after the root element is removed. To remove the root while maintaining the complete binary tree property, the last element in the array is swapped with the root. The last element is then removed. The new element at the root, which was formerly a leaf, will likely violate the heap property.
    - The goal of heapify-down is to move the new root element down the tree until it finds its correct position and the heap property is restored. The process involves:




    - Start at the root: Begin with the element at the top of the tree (or any node that needs to be "fixed").
    - Compare with children: Compare the element with its children.
    - Find the "correct" child:
        In a max-heap, find the child with the largest value.
        In a min-heap, find the child with the smallest value.
    - Swap if necessary: If the element is violating the heap property (e.g., in a max-heap, it is smaller than its largest child), swap it - - with the child that you found in the previous step.
    - Repeat: After the swap, the element is now at a new position. Repeat the comparison and swapping process with its new children.
    - Stop condition: The process stops when one of two conditions is met:
    - The element reaches a leaf node.
    - The element is no longer violating the heap property (i.e., it is in the correct position relative to its children).


- In a binary heap, which is a complete binary tree, there is a direct relationship between the level of a node and the maximum number of nodes that can exist at that level. This relationship is based on powers of 2.
- relation between level and binary tree is (2 ** L + 1) - 1 
- for level 0 = 1
- for level 1 = 2
- for level 2 = 4
- for level 3 = 8
- for level 4 = 16
- for level 5 = 32



- Heapify : The core heapify operation is a recursive process that fixes the heap property at a single node. Given an array representing a heap and the index of a node to fix, the algorithm works as follows:
    - Find the largest/smallest: For a max-heap, compare the value of the current node with its left and right children to find the largest among the three. For a min-heap, find the smallest.
    - Swap if necessary: If the largest/smallest value is not the current node, swap the current node with that child.
    - Recursively heapify: After the swap, the child's subtree may now violate the heap property. Recursively call heapify on the child's new index to fix the subtree.

Building a Heap from an Array :
    - Find the last non-leaf node: In an array of size N (with 0-based indexing), the last non-leaf node is at index ⌊(N/2)−1⌋. All nodes after this index are leaf nodes, which are already considered valid heaps of size one.
    - Iterate and heapify: Loop through the array indices backward, from the last non-leaf node down to the root (index 0). At each index, call the heapify function.


heap sort :
- comparisons based sorting algo utilize the heaps 
- sorting can be accending or decending 
- for accending order - use max heap 
- decending order - use min heap 
- build the max heap 
- repetedly take largest element place it at end of array 
- get the largest and reduce heap size by 1 
- decrease freq by 1 
- After all extractions, the array is sorted in ascending order.




Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity: O(1) (in-place sorting)
# https://g.co/gemini/share/4ff78b649597