"""
The "Kth Largest Element in a Stream" problem asks you to design a class that finds the kth largest element in a continuously 
flowing stream of numbers. Unlike finding the kth largest element in a static array, here the set of numbers is constantly changing as 
new elements are added. The key is that the value of k remains fixed, but the list of numbers you're considering grows with each new element.

A naive approach would be to store every single number in a list, sort the list whenever a new number is added, and then return the 
element at the k-th position from the end. This is highly inefficient due to the cost of sorting, which is O(NlogN), where N is the number 
of elements in the stream.

A more efficient way to solve this is to maintain a data structure that keeps track of only the k largest elements seen so far. This 
significantly reduces the storage and computation required.


The most efficient and widely used solution involves a min-heap (also known as a min-priority queue). A min-heap is a binary tree-based data 
structure where the value of each parent node is less than or equal to the values of its children. This property means that the smallest 
element is always at the root of the heap.


The strategy is as follows:

Initialization: When you initialize the KthLargest class with a value k and an initial array of numbers nums, you create a min-heap. You then 
insert all the numbers from nums into this min-heap.

Maintaining the Heap Size: The crucial step is to ensure that the size of the min-heap never exceeds k. After inserting a number, 
if the heap's size becomes greater than k, you remove the smallest element from the heap (which is always at the root) by performing a pop or extract-min operation.


Adding a New Element: When a new number val is added to the stream via the add() method, you insert val into the min-heap. Again, 
if the heap's size grows beyond k, you remove the smallest element.


Finding the Kth Largest Element: After an add() operation, the min-heap will contain exactly the k largest elements seen so far. The smallest element among these k elements is, by definition, the kth largest element in the entire stream. Since the min-heap always keeps its smallest element at the root, you can simply return the root element of the heap.

The goal is to keep track of the k largest elements at any given time. A min-heap is perfect for this task because it's designed to keep the smallest 
element at the top (root).

We maintain a min-heap with a maximum size of k.
When a new number arrives, we add it to the heap.
If the heap size exceeds k, we know we have more than the top k elements. The element that doesn't belong in our group of the top k is the smallest one.
Since our data structure is a min-heap, the smallest element is always at the root. So, we simply pop the root element.
After this operation, the heap contains exactly the k largest elements seen so far. The smallest of these k elements is by definition the kth largest element overall.



Why a Max-Heap Would Be Inefficient
Using a max-heap would be a much less optimal approach. A max-heap's main purpose is to give you the largest element quickly.
A max-heap would have to store all the numbers in the stream to know which one is the kth largest. You would keep adding numbers to the heap 
as they arrive.
To find the kth largest element, you would have to pop the largest element k-1 times, then look at the root.
This would be very inefficient for two reasons:
Space: The heap would grow to the size of the entire stream (O(N)), which could be massive.
Time: Each add operation might require multiple pop operations to get to the kth largest, and the heap itself would be constantly changing, making each operation take more time as the heap grows larger.

In summary, a min-heap of size k is a clever way to solve this problem by focusing only on the data you need to track, while a max-heap would require you to keep track of everything and then filter down, which is much slower.








"""



import heapq
class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums :
            heapq.heappush(self.min_heap , num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap) 
        

    def add(self, val: int) -> int:

        heapq.heappush(self.min_heap , val)
        if len(self.min_heap) > self.k :
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
