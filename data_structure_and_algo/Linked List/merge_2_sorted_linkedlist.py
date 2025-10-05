"""
Given 2 Linked list sorted merge tham 
we have to use orignal nodes 
we cant create a new copy duplicate node 


- The main challenge in building a new linked list is handling the very first node (the new head). The Dummy Node technique solves this by 
creating a temporary placeholder node that precedes the actual head of the merged list.
- Initialization: Create a dummy node and set a tail pointer to it. Let l1 and l2 be the heads of the input lists.
- Traverse and Compare: While both l1 and l2 are not empty:
- Compare the values of the current nodes: l1.val and l2.val.
- Append the Smaller: Set tail -> next to the node with the smaller value.
- Advance: Move the pointer of the list from which the node was taken (either l1 or l2) to its next node.
- Move Tail: Advance the tail pointer to the newly added node (tail = tail -> next).
- Append Remaining: Once the loop finishes, one of the lists might still have remaining nodes (since they are already sorted). Attach the entire remainder of the non-empty list to the end of the merged list:





"""
from typing import Optional




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2 :
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else :
                node.next = list2
                list2 = list2.next
            
            node = node.next 
        
        node.next = list1 or list2

        return dummy.next
        