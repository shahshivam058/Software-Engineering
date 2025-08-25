class Solution:
    def countOddDigit(self, n):
        OddCount = 0 
        if n == 0 :
            return 0 

        while n > 0 :
            last_digit = n % 10 
            if last_digit % 2 != 0 :
                OddCount += 1 
            n = n // 10 

        return OddCount            