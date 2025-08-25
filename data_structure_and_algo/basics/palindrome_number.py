class Solution:
    def isPalindrome(self, n):
        if n < 0 :
            n = -n 

        originalNumber = n
        ReversedNumber = 0 

        if n < 10 : # single digits are always palindrome 
            return True

        while n != 0 :
            lastDigit = n % 10 
            ReversedNumber = (ReversedNumber * 10 ) + lastDigit
            n = n // 10 

        return originalNumber == ReversedNumber
    

