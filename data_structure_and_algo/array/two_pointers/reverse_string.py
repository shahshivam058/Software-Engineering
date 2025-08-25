"""
You are given an array of characters which represents a string s. Write a function which reverses a string.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["n","e","e","t"]

Output: ["t","e","e","n"]


Below one is efficient way to solve the problem 

Input string that is given need to reverse that
array is simple 

take the end to begining and vice verca 
The main funda is we are swapping 2 diff values to form array 
if string is even length then both pointer will cross each other 
if odd then meet at middle 


we can use stack and push all element to stack 
when we remove from stack and add element to last and the result one is reverse array

we are pushing all elements to stack and then pop and add it index 
for c in chars:
    stack.append(c) $ w

while stack and i < n :
    s[i] = stack.pop()
    i += 1

we can use recursion 


        def reverse(l, r):
            if l < r:
                reverse(l + 1, r - 1)
                s[l], s[r] = s[r], s[l]

        reverse(0, len(s) - 1)


"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        while start < end :
            s[start]  , s[end] = s[end] , s[start]
            start += 1
            end = end - 1
        
        return s