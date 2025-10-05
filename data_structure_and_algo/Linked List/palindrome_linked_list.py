"""
Reverse of string is same as actual string 

same for linked list reversal of linkedlist same as orignal linked list 

return True : If Palindrome else false 
we have to do it without any extra space 

Brute force approch :
- add all elements to array and apply two pointer approch on the same 

Brute force 2 :
utilise the stack 


we can add all values to stack and while
now the value that got add last is nothing but end of linked list 
so proper reversal of linkedlist stored in stack 

pop from stack compare with element in linked list and return 


Optimal approch 
slow pointer and fast pointer 
now we have pointer in middle as well as end 
we will also have at start of linkedlist
reverse from middle to end linked list 
loop from start and reverse compare values 
"""



from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left = head
        right = prev

        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
