class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF # A 32-bit mask used to handle overflow

        for i in range(32): # Loop over 32 bit in integer
            a_bit = (a >> i) & 1 # for each bit shift by left and check 1 or 0 
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry # do sum 
            carry = (a_bit + b_bit + carry) >= 2 # check if there is carry than returns 1 
            if cur_bit:
                res |= (1 << i) # add to result 

        if res > 0x7FFFFFFF: # the maximum positive 32-bit signed integer, 2^31 - 1
            res = ~(res ^ mask) # flips all 32 bits of res (since mask = 0xFFFFFFFF). inverts all bits again (including higher bits beyond 32), but due to Python's arbitrary-precision integers, we effectively get the 32-bit signed negative number.



            
        return res
