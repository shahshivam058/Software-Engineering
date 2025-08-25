class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        carry = 0 
        i = len(num) - 1
        result = []

        while i >= 0 or k > 0 or carry > 0  : 
            digit = k % 10 
            sumval = carry + (num[i] if i >= 0 else 0) + digit 
            result.append(sumval % 10)
            carry = sumval // 10

            k = k // 10 
            i = i - 1

        result = result[::-1]
        return result