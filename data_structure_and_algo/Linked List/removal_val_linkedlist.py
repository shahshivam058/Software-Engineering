"""
Remove all the oocurances from linkedlist 

Output will be linkedlist without that particular value 

Create a nothing but a new dummy node which points to head 
assigned dummy node to prev 
and head to curr 
Loop Untill the end of linked list 
store the next node refrance of  current 
check if current value similer as new value target means we have to remove pointer 
previous node pointer will point to next node if values are same 
else just change the prev will be current now 

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy  = ListNode(0 , head)
        prev = dummy
        curr = head 

        while curr :
            nxt = curr.next 
            if curr.val == val :
                prev.next = nxt 
            else :
                prev = curr 
            
            curr = nxt 
        
        return dummy.next