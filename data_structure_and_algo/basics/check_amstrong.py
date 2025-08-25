# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


# Examples:
# Input: n = 153
# Output: true
# Explanation: Number of digits : 3.
# 13 + 53 + 33 = 1 + 125 + 27 = 153.
# Therefore, it is an Armstrong number.

# Input: n = 12
# Output: false
# Explanation: Number of digits : 2.
# 12 + 22 = 1 + 4 = 5.
# Therefore, it is not an Armstrong number.




class Solution:
    def isArmstrong(self, n):
        originalNumber = n 
        NumberLength = 0 
        temp = n 

        while n != 0 :
            NumberLength += 1
            n = n // 10
        
        Result = 0 
        while originalNumber != 0 :
            lastDigit = originalNumber % 10 
            Result = Result + (lastDigit ** NumberLength)
            originalNumber = originalNumber // 10 
        
        return Result == temp
