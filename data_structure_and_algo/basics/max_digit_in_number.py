class Solution:
    def largestDigit(self, n):
        MaxDigit = 0 

        if n < 0 :
            n = -n 

        if n < 10 :
            return n 

        while n != 0 :
            lastDigit = n % 10 
            MaxDigit = max(MaxDigit , lastDigit)
            n = n // 10 
        
        return MaxDigit