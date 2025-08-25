class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right
    
"""
right &= right - 1 removes the rightmost 1 bit from right.
We keep doing this until right <= left.
Why? Because any differing bits between left and right will become 0 in the final result (due to AND).
So we just keep trimming right until it matches left in the higher bits.
"""
