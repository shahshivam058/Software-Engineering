class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32): # as we are working with 32 bits integer
            bit = (n >> i) & 1 # check if i bit is 0 or not 
             # place bit at actual location and accumelate result 
        return res
    

# (bit << (31 - i))

"""
(bit << (31 - i))

bit = bit we want to place it can be either 1 or 0 
(31 - i ) represents the location where we place to bit 

(bit << (31 - i)) we are doing left shift to place bit at designated location 

🧮 Why +=?
Because we do this in a loop, and we're accumulating the bits one at a time into res.

Initially, res = 0
First iteration: Add the reversed bit for i = 0
Second iteration: Add the reversed bit for i = 1
...
Last iteration: Add the reversed bit for i = 31


we can also write res |= (bit << (31 - i))
"""