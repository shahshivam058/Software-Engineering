"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



we have to stor element somewhere to keep all unique elements so far thats why we use set here 
and insilized the l = which may represent the starting window 

now we are looping from first char to last element in a string 
new char is not part of set means we havent got this char so far so we can add to 
if we got a char which is in set then  we have to remove all element in till char and including char 
so that we can add a new element in left  
the reason we are not just removing particular element and all element til current element including current element is we need a substring means continous part of string if we only remove char than it would not form a substring 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l = 0 
        max_length = 0 


        for index in range(len(s)) :
            while s[index] in window :
                window.remove(s[l])
                l = l + 1
            
            window.add(s[index])
            max_length = max(len(window) , max_length )

        

        return max_length

