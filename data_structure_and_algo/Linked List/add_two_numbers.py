# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0 
        curr = dummy 

        while l1 or l2 or carry :
            a = l1.val if l1 else 0 
            b = l2.val if l2 else 0 

            total_sum = a + b + carry 
            carry = total_sum // 10
            val = total_sum % 10 

            curr.next = ListNode(val)
            curr = curr.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        
        return dummy.next 
