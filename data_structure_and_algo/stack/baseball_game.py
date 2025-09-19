from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0 
        stack = []

        for op in operations :
            if op == "+" :
                result = result + stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                result = result + (2 * stack[-1])
                stack.append (2 * stack[-1])
            elif op == "C":
                result = result - stack.pop()
            else :
                result = result + int(op)
                stack.append(int(op))

        return result     






                