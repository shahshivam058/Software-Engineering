"""
way we can perform arithmatic opretions 
RPN Always Gonna be valid 


we are going to be reading from left to right 
when we reach opretor apply to 2 previous values 
replace them with actual value 

"""


from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token ==  "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif token == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif token == "*" :
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif token == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b / a)
            else :
                stack.append(token)
        
        return int(stack[-1])
