"""

- Next Smaller Element Left / Right : Maintain Increasing order Monotonic stack to build result array
- Next Greter Element Left / Right : Maintain Decresing order Monotonic stack to build result array

- The main aim of maintaining the incresing order in monotonic stack is we have to search for smaller elements on left so if there is element on top of stack greter then current element it will not maintain monotonic stack .
- The main aim of maintaining the decresing the monotonic stack is we want bigger element a bigger element if element in stack less current element then pop that 


- Next Smaller Element (Left / Right)

    - Stack type: Monotonic Increasing (from bottom → top).

    Why:
    - We are looking for a smaller element.
    - If the element on top of the stack is greater than the current element, it cannot be the “next smaller,” so we pop it.
    - By doing this, the stack always remains in increasing order.
- Next Greater Element (Left / Right)

    Stack type: Monotonic Decreasing (from bottom → top).

    Why:
        - We are looking for a greater element.
        - If the element on the stack is smaller than the current element, it cannot be the “next greater,” so we pop it.
        - By doing this, the stack always remains in decreasing order.


"""



class Solution:
    def nextSmallerElements(self, arr):
        n = len(arr)
        result = [-1] * n 
        stack = []

        for i in range(n - 1 , -1 , -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            
            if stack :
                result[i] = stack[-1]
            
            stack.append(arr[i])
        
        return result
            

