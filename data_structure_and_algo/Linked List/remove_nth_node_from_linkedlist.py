"""
Given a linked list of size n

return the Nth node from linked list and return the head of linked list 
keep 2 pointer 
space between two pointer keep n so one reaches end another reaches end -n 
The only thing to delete that node point to next.next 
we are adding dummy node to and start left from there just to reach node before 

first we reach nth distance on linked list 
start from dummy node 
when right reaches end left reaches the node before one to be remove 
just change pointer and done 


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        left = dummy 
        right = head 

        while n > 0 :
            n = n - 1
            right = right.next
        
        while right :
            right = right.next 
            left = left.next
        
        left.next = left.next.next

        return dummy.next