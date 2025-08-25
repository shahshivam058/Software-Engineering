"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).



we are skipping all alphanumeric means we are skipping space 


remove all other signs remove question mark and space and only chars combine them if reversal of that same than return true else false 


Brute Force Solution :

for each char we can check if its alphanumeric then append ton string the genrated string will be reversal of string 
then just reverse the string directly or use slicing and check if string same as string reversal 
In interview they might not want to use alphanumeric function and 


we have to solve problem without using extraspace 
0(1)



Optimal Approch :

Use 2 pointer 

left and right pointer 
compare lect and right and change posi
we want to ignore all the non alphanumeric chars 
we can do it without using isalnum function 
check if each symbol either between 0 to 9 or a to z or A TO Z
Just compar the current char if within alphanumeric range or not 

we can write a while loop to skip all the non alphanumeric to skip  
string might meet in middle 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]




class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]): # not self.alphaNum(s[l]) : Means self.alphaNum(s[l]) in case of alphanumeric return true and we only want to move in non alphanumeric so loop will execute everytime we are using not incase of alnum return true and loop got executed 
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): # char can be uppercase or lower case so convert both to lowercase 
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):  # we are checking using this function if char is alphanumeric or not if char in string in alphanumeric then skip the char
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))