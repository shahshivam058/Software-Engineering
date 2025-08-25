class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #your code goes here
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamped to 32-bit int max
    
    # Determine sign
        negative = (dividend < 0) != (divisor < 0)
        
        # Convert to positive long for safety
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0 

        for i in range(31,-1,-1) :
            if ( divisor << i) <= dividend :  # we check if we check if multiple of divisor < dividend or not  ( divisir * 2 ^ i ) that is multiple of divisor 
                result = result + (1 << i) # add to actual anwser as it is part of anwser
                dividend = dividend - (divisor << i) # subtract from dividend 

        return -result if negative else result


"""
we loop from 31 bit to 0th bit 
we check if multiple of divisor < then dividand or not 
if its lessthan then its part of anwser 
add that to result and then subtrect from dividend 
"""