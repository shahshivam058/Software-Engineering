"""
LeetCode : https://leetcode.com/problems/score-of-a-string/description/

You are given a string s. The score of the string is defined as the sum of the absolute differences between the ASCII values of adjacent characters.

Concept:
    For each pair of adjacent characters in the string, calculate the absolute difference between their ASCII values.
    The absolute difference means the result is always non-negative (i.e., positive or zero).
    To calculate this, convert each character to its ASCII value using ord(), then take the difference and apply abs() to get the absolute value.
    Loop through the string starting from index 1 to n-1, and for each position, subtract the ASCII value of the previous character from the current one, take the absolute value, and add it to the result.
    Finally, return the total sum as the score.


"""

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        n = len(s)
        for i in range(1 , n) :
            result += abs( ord(s[i - 1]) - ord(s[i]) )      

        return result   