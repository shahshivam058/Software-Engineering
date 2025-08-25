# Check for Perfect Number

# You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.

# A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.


# Examples:
# Input: n = 6
# Output: true
# Explanation: Proper divisors of 6 are 1, 2, 3.
# 1 + 2 + 3 = 6.

# Input: n = 4
# Output: false
# Explanation: Proper divisors of 4 are 1, 2.
# 1 + 2 = 3.


class Solution:
    def isPerfect(self, n):
        perfectnumber = 0 

        for i in range(1,n) :
            if n % i == 0 :
                perfectnumber = perfectnumber + i 
        
        return perfectnumber  == n 
