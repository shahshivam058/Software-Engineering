"""
You are given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

each char represents a column number 

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Convert base 10 number to column representation 

each char or each place possibality of a - z 
first char map to 1 
we can easuly get A + number = gives result 

we can get % 26 which returns the value within 26 
with help of that we can first char 



Excel column titles look like they’re base-26, but there’s a twist.
A … Z = 26 letters (like digits 1 … 26)
After Z, it becomes AA, not BA or A0.
This is different from usual base systems (like binary or decimal) where digits start from 0.
Here, letters start at 1 (A) instead of 0.

So, the system is 1-indexed, not 0-indexed.


Think of converting columnNumber to base-26.
But since Excel is 1-indexed, we need to shift things:
Normally: base-26 digits are 0–25.
In Excel: digits are 1–26.

So:

A should represent 1 (not 0).
Z should represent 26.
After Z, the cycle continues → AA.
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            res += chr(ord('A') + offset)
            columnNumber //= 26

        return ''.join(reversed(res))