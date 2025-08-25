class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        xorsum = start ^ goal 
        count = 0 
        while xorsum :
            xorsum = xorsum & (xorsum - 1)
            count += 1 
        
        return count 

# The number of differing bits between a and b is equal to the number of bit flips needed.
# This can be found using XOR (^):

# XOR returns 1 where bits differ and 0 where they match.

# Counting the 1s in a ^ b gives the answer.

