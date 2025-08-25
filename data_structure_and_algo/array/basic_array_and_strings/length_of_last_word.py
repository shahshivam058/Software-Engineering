"""
https://leetcode.com/problems/length-of-last-word/description/

Brute‑Force Approach:

    Start from the first character.
    Loop through all characters:
    If it's not a space, increment length.
    If it's a space, reset length to 0.
    At the end, return length (which represents the length of the last word).

Optimized Backward Approach:
    Starting from the last character, skip all trailing spaces.
    Once you hit a non-space character, start counting.
    Stop counting when you reach a space or the start of the string.
    Return the count.
    There is a  base case check if we reached at first char or not 

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0 
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i = i - 1
        
        while i >= 0 and s[i] != ' ':
            length += 1
            i = i - 1
        
        return length