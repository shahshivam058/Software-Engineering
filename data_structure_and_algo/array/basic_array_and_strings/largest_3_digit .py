"""
Leet code Link : https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.


Brute force approch :we can use an brute force approch  use sliding window form a string convert to a string and compare
optimal approch : slightly better approch we can use is we know 3 digits we need to compare in a string just check and compare current with next one and digit after next one check if same or not if same then compare with last one 



best = compare 3 digit if same then convert to int and check mnax and return max * 3
"""




class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        result = "0" 
        for i  in range(len(num) - 2) :
            if num[i] == num[i+1] == num[i+2]:
                result = max(result , num[i : i + 3]) # nums[i : i + 3] allows us to get all 3 digits we can compare current 3 digits if all are same with last result anyway it will compare lexographical order 
        
        if result == "0" :
            return ""
        return result


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, int(num[i])) # just compare first element with last  best element all 3 element will be same by anyway so just compare 2 digits 1st digit of current 3 group digit or last one result 

        return str(res) * 3 if res != -1 else "" # when found *3 which return 3 digits string 
