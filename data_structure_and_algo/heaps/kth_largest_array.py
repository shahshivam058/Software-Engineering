"""
using bubble sort 

sort till kth element and return 


minheap : 

This function is the core of the operation. It finds and returns a list containing the k largest items from the iterable nums. 
The crucial part is that it does this without sorting the entire list.

Under the hood, heapq.nlargest uses a min-heap of size k. As it iterates through the list nums, it maintains a heap containing the k largest 
elements seen so far. This process is much faster than a full sort, especially when k is significantly smaller than the total number of 
items.

The list returned by this function is sorted in descending order (from largest to smallest).



heapq.nlargest(k, nums) finds the k largest numbers and returns them in a sorted list.
The k-th largest element is, by definition, the smallest of these k largest numbers.
Since the list is sorted in descending order, the k-th largest element is located at the very end of the list.
The [-1] index perfectly selects this final element, which is the answer.




"""

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]