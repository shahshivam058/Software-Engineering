class Solution:
    def countDigit(self, n):
        count = 0 
        if n == 0 : # the edge that can be missed as we are running loop till 0 
            return 1

        if n < 0 : # Just check edge case if number is negative convert to positive 
            n = -n 
         
        while n > 0 :
            count = count + 1
            n = n // 10 
        
        return count 
