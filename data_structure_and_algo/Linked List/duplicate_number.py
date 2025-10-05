"""
Given an array consist of integers n + 1
where each integer 1 to n 
One repeted number return that 

Simplest :
use hashset 


another simplest :
utilise the  sorting 
compare each element with next element 

This Is linked List problem 
floyd algo 

len = n + 1
nums[i] in [1 , n]

Think in term of pointer 


each number is in range of array length 
each number might point to an an index an array 
none of them point outside range 
if two number point to same number there are multuple node 2 

if something form cycle then duplicate exist 

start of cycle is nothing but an anwser 

floyd algo  to get begaining of cycle 

use the slow and fast pointer find first intersection 
then use 2 slow pointer and both shift by 1 where they meet its intersection point 




How the Algorithm Works for Duplicate Detection
The key idea is to treat the array's indices and values as a linked list structure:

The index represents the current node.

The value at that index represents the next node to visit. That is, if you are at index i, the next "node" you go to is index nums[i].

Since the array has n+1 numbers from 1 to n, there must be a duplicate number. This duplicate forces the sequence of jumps to eventually enter a cycle.

1. Cycle Detection (Phase 1)
This phase uses the two pointers to find a meeting point within the cycle.

Slow Pointer: Moves one step at a time (slow=nums[slow]).
Fast Pointer: Moves two steps at a time (fast=nums[nums[fast]]).
Initialization: Both pointers start at index 0.
The pointers are iterated until they meet. The meeting point is guaranteed to be inside the cycle.

2. Finding the Cycle's Start (Phase 2)
The duplicate value is the starting point of the cycle.
Reset: Reset the slow pointer back to the initial starting position (index 0). The fast pointer remains at the meeting point found in Phase 1.
Iteration: Move both pointers one step at a time (slow=nums[slow] and fast=nums[fast]).
Meeting Point: The point where they meet again is the entrance to the cycle, which is the duplicate number.




"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 

        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break 
        
        slow1 = 0 
        while True : 
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow == slow1:
                return slow 
        