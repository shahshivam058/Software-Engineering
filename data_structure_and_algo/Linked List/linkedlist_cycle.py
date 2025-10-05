
"""
This phase determines if a cycle exists in the list by using two pointers that move at different speeds.


when we are using slow fast pointer then we have to check Loop while the fast pointer can still move two steps forward
Key Pointers
- Slow Pointer (Tortoise): Moves one step at a time (slow=slow→next).

- Fast Pointer (Hare): Moves two steps at a time (fast=fast→next→next).

Logic

- No Cycle: If the list is linear, the fast pointer will eventually reach the end of the list (NULL), and the algorithm terminates, 
  returning false.
- Cycle Exists: If there is a cycle, the fast pointer is guaranteed to eventually catch up to the slow pointer inside the loop. When 
  they meet, it confirms that a cycle exists. This happens because the relative speed difference is 1 (Fast moves one step closer to Slow each iteration).


Middle Linked List 
This technique uses two pointers, often called "slow" (the Tortoise) and "fast" (the Hare), which traverse the list at different speeds.

Slow = 	1 step per iteration (slow=slow→next)	    = Reaches the middle when Fast reaches the end.
Fast =	2 steps per iteration (fast=fast→next→next) = Reaches the end of the list first.


Algo To find Loop Starting 
Reset One Pointer: Keep the fast pointer at the Meeting Point (M) where the collision occurred. Reset the slow pointer back to the Head of the linked list.
Move at Same Speed: Move both slow and fast pointers one step at a time until they meet again.
Collision Point: The node where they meet the second time is the Start of the Cycle (C).


"""


# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head 

        while current :
            if current in seen :
                return True
            seen.add(current)
            current = current.next
        
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 

        # we will Loop Untill there is node 2 step ahead 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast :
                return True
            
        return False



def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    # The loop condition ensures 'fast' can move two steps
    while fast and fast.next:
        slow = slow.next      # Moves 1 step
        fast = fast.next.next # Moves 2 steps
        
    # When the loop finishes, 'slow' is at the middle node
    return slow