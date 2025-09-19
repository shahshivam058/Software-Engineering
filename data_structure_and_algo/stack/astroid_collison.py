"""
arr = [5 , 10 , -5]:


5 : Moving to right 
10 : Movie to right 
-5 : Movie to left  

10 and -5 both colied small one gona colied 
result is 5 and 10 


Positive Means Going to right 
Negative means left
absolute value represents the size of astroid 

if 2 astroid meets smaller one will be destoryed
if both are same then both are destroyed


"""


from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # Handle collisions only if current asteroid is moving left else if going right directly add 
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:   # top asteroid is smaller, it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:  # both explode
                    stack.pop()
                break
            else:
                stack.append(a)
        
        return stack
