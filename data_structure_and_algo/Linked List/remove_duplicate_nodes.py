"""
The main aim to remove duplicate Nodes from Linked List 

we may create a curr which point to head which is start of linked list 

Loop till the end of linked list 
compare the current node value with next node value 
if both value are same then curr will point to 2 nodes ahead 
else we will increase the curr 
do it till end of linked list 

curr.next = curr.next.next  when we want to change the pointer where it point 
curr = curr.next.next 

when .next is on left means we are changing the pointer 
when .next is on right means we are changing the location 

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        while curr and curr.next :
            if curr.val == curr.next.val :
                curr.next = curr.next.next
            else :
                curr = curr.next
        
        return head
        