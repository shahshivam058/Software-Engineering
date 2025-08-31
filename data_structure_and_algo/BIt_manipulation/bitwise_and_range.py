"""
We need:

result=left & (left+1) & (left+2) & ... & right

Where & is the bitwise AND operator:

1 & 1 = 1

1 & 0 = 0

0 & 1 = 0

0 & 0 = 0

Key property:

Bitwise AND tends to "zero out" bits quickly.
If any bit position becomes 0 in one number, it stays 0 in the final result (since AND with 0 is always 0).

If left == right, then result is just left (only one number).
If right is much larger than left, many bits will eventually turn 0.

🔎 Step 3: The Trick (right &= right - 1)

This is a classic bit manipulation trick:

x & (x-1) removes the lowest set bit from x.


Condition: Run while left < right.

Meaning: While the range has more than one number.

What happens inside?

We keep clearing the lowest set bit of right.
This gradually reduces right downward toward left.
The goal is to find the common prefix in the binary representations of left and right.
Any differing lower bits (below the highest differing bit) will definitely become 0 in the AND result.

The algorithm:

Start from right.

Repeatedly clear its lowest set bit until it is no longer larger than left.

At this point, the number (right) only has the stable prefix bits left — which is the correct result.
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right :
            right &= (right - 1)
        return right