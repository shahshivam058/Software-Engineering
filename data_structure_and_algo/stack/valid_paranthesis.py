class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 :
            return False

        stack = []
        brackates = {"(" : ")", "[" : "]" , "{" : "}" }

        for char in s :
            if char in  brackates.keys() :
                stack.append(char)
            else :
                if not stack or brackates[stack[-1]] != char:
                    return False
                stack.pop()
        
        return len(stack) == 0
