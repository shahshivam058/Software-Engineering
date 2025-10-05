"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Brute force approch :

Brute force approch we can store all values in array 
use 2 pointer approch 


we will use begaining of a list and merge with 2nd half of linked list 
reverse the 2nd part of lined list 



Find Middle of linked List 

- This step uses the slow and fast pointer technique (also known as the tortoise and hare algorithm).
- Initialize two pointers, slow and fast, both starting at the head.
- In each iteration, advance slow by one step and fast by two steps (fast = fast.next.next).
- When fast reaches the end of the list (or None), slow will be at the middle node (or the node just before the start of the second half).
- This effectively splits the list into two halves: the first half starting at head, and the second half starting at slow.next. The link between slow and slow.next is then broken by setting slow.next = None to terminate the first half.


The second half of the list are now at the front of this new list.

Use the iterative reversal method with three pointers (prev, current, temp) to reverse the direction of the links in the second half.




The final step is to combine the original first half

Iterate as long as the second list (List B) has nodes.

In each iteration, you take the next node from List A and the next node from List B, and perform the following sequence of links:

List A's current node points to List B's current node.

List B's current node points to List A's original next node.

This interleaving is done in-place to achieve the desired reordering:





"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # <-- FIX: Fast pointer must advance by two

        # 'slow' is now at the start of the second half (or the node just before it)

        # 2. Split the list and reverse the second half
        second = slow.next 
        slow.next = None  # Terminate the first half
        
        # Reverse the second list (standard iterative reversal)
        prev = None 
        current = second
        while current:
            tmp = current.next 
            current.next = prev 
            prev = current 
            current = tmp 

        # 'prev' is now the head of the reversed second half

        # 3. Merge the two lists
        first = head
        second = prev # Head of the reversed second half

        while second:  # We only need to iterate as long as the second list has nodes
            temp1 = first.next 
            temp2 = second.next 

            # Interleave the nodes: first -> second -> (original first.next)
            first.next = second
            second.next = temp1

            # Advance pointers
            first = temp1 
            second = temp2