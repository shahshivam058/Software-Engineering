"""
680. Valid Palindrome II - Explanation
Problem Link

Description
You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

A palindrome is a string that reads the same forward and backward.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Brute force approch :
first check if string is palindrome or not 
check by remove each char if string if palindrome or not 
o(n**2)


suppos if we got 

aaaz 

first and last char are not the same 
we alloed to remove one of char to make palindrom 
it can be first or last 
we dont know which char first or last so we can try with both 
we will 
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1] # will skip first char from left 
                skipR = s[l : r] # will skip right char 
                return skipL == skipL[::-1] or skipR == skipR[::-1] # if any of by removing one char still if its not palindrome then we are returning false if one of it is paildone means we fulfilled and returning true 
            l, r = l + 1, r - 1

        return True




"""
Rather than using above concept where code looks messay we are just  created a small helper function and we are using that and comparing if palindrome or not 


"""
class Solution(object):
    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # try skipping either side once
                return self.is_palindrome(s, l + 1, r) or self.is_palindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True
