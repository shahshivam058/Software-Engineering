"""
Identify the intersection point of linked list 

Loop Through One linked list store all the nodees
start from another head check if new node part of hashset its the ans 


identify the length of both linked list 
for one which has less node reach to correct locatoon and then loop and start comparing 

"""


# Definition for singly-linked list.
# class ListNode:
#      def __init__(self, x):
#          self.val = x
#          self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # 1. Helper function to find length
        def getLength(head):
            length, cur = 0, head
            while cur:
                length += 1
                cur = cur.next
            return length

        m = getLength(headA)
        n = getLength(headB)
        l1, l2 = headA, headB

        # 2. Swap to ensure l1 is the head of the longer list
        if m < n:
            m, n = n, m
            l1, l2 = headB, headA

        # 3. Advance the pointer of the longer list (l1) by the difference in length
        while m - n:
            m -= 1
            l1 = l1.next

        # 4. Traverse both lists simultaneously until the pointers meet
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        # l1 (or l2) is the intersection node, or None if no intersection
        return l1
    

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB

        while l1 != l2 :
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1