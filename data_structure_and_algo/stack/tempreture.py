"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

we just need to maintain monotonic stack decresing order like its really similer to next greter element on right


we are just maintaining indexes in our stack 
Traverse temperatures from right to left.
(So we always look at the "future" days first.)

For each day i:

Pop from the stack while the top has a temperature less than or equal to temperatures[i] (since those can’t be the next warmer day).

If the stack is not empty, the top of the stack gives the next warmer day.
→ So result is stack.top - i.

Push i onto the stack.


i = current day
stack[-1] = index of the next warmer day
The stack gives us the index of the warmer day.

The problem wants the number of days to wait.

Subtraction (stack[-1] - i) converts an index difference into a day count.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n 
        stack = []

        for i in range(n - 1 , - 1 , - 1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i
        
            stack.append(i)
        
        return result