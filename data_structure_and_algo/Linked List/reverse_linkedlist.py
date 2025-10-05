"""
Reverse a Linked List :



prev (or previous): Stores the node whose next pointer has already been reversed. Initially, this is NULL (or nullptr) because the new head (the original tail) should point to nothing.
current: Points to the node being processed. It initially points to the head of the original list.
next_node (or temp): Temporarily stores the next node before the current node's next pointer is changed. This is crucial for maintaining a link to the rest of the list.

we will take next pointer and reverse it 
for first node next pointer will be point to null 

- We have to Loop till we havent processed all the nodes in the list.
- each loop we need to store ref to next node 
- once we have refrance of next node then safe to process current node 
- then for current node change the pointer to prev which presents the previous node 
- then we have to store the location of node that one is processed which is current 
- then just assign new node to be processed to current 
- prev pointer will be new head in the end 

"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        current = head 

        while current :
            temp = current.next
            current.next = prev 
            prev = current 
            current = temp

        return prev
