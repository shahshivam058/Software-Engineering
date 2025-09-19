"""
This dictionary maps Roman numeral symbols to their integer values.
We start with a running total (res) set to 0.
Loop through each character in the string s.
Here’s the subtraction rule:

If the current numeral is smaller than the next numeral, subtract it.
Example: In "IV", I (1) is less than V (5), so subtract 1 instead of adding it.
Otherwise, just add the current numeral’s value.
At the end, return the total.

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

