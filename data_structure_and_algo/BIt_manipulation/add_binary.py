class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry > 0: # we are looping over both a and b string and  max no of loops is max of both strings 
            digitA = int(a[i]) if i >= 0 else 0 # convert to Integer 
            digitB = int(b[j]) if j >= 0 else 0 # convert to Integer 


            total = digitA + digitB + carry # add to total 
            res.append(total % 2) # add actual total in binary  % 2 returns sum and / 2 returns carry 
            carry = total // 2

            i -= 1
            j -= 1

        res.reverse()
        return ''.join(map(str, res))
    

# When we process the binary strings a and b, we start from the end (least significant bit, or rightmost digit) and move to the beginning (most significant bit, or leftmost digit).
# As we compute each digit, we append() it to the res list. This means the first digit we compute (the rightmost digit) goes first in the list, and the last digit we compute (the leftmost digit) goes last in the list.
# However, binary numbers are read from left (most significant bit) to right (least significant bit), so we need to reverse the list to get the correct order.



class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        i, j = len(a)-1, len(b)-1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result = str(total % 2) + result
            carry = total // 2
            
        return result
