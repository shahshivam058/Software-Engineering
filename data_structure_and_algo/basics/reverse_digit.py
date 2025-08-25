class Solution:
    def reverseNumber(self, n):
        ReversedNumber  = 0 
        if n < 0 :
            n = -n 
        
        while n  != 0 :
            lastDigit = n % 10
            ReversedNumber = (ReversedNumber * 10) + lastDigit
            n = n // 10 
        
        return ReversedNumber
