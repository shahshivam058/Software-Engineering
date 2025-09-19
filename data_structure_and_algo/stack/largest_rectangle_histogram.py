"""
The Problem
Imagine a bar chart. You need to find the largest rectangle that can be drawn under the tops of the bars. This rectangle could be a single bar, or it could stretch across multiple bars, where its height is constrained by the lowest bar in that group.
For example, given the heights [2, 1, 5, 6, 2, 3]:
A rectangle with height 1 would have a width of 6 (the entire histogram), giving an area of 6.
A rectangle with height 2 could span across the last three bars (2, 3), with the height limited by 2, giving an area of 2 * 3 = 6.
The largest rectangle, however, has a height of 5 and spans across the bars with heights 5 and 6, giving a width of 2 and an area of 10.

The most efficient solution uses a monotonic stack. The key idea is that for any given bar, the largest rectangle that uses this bar 
as its height can extend to the left and right until it hits a bar that is shorter than it. The monotonic stack helps us find these 
"next smaller" and "previous smaller" elements in a single pass.

- Iterate through the bars: Process the histogram from left to right.
- Maintain a monotonic stack: The stack will store the indices of the bars. The stack maintains an invariant that the heights of the 
bars at the stored indices are always in increasing order.
- Calculate Area on Pop: When you encounter a bar that is shorter than the bar at the top of the stack, it signifies that the bar at the top of the stack can no longer extend further to the right. This shorter bar acts as the right boundary.
    - You pop the index from the stack.
    - The popped index's bar height is the height of your potential rectangle.
    - The width is calculated as the difference between the current index and the new top of the stack's index (minus one).
    - Calculate the area and update the max_area.
- Push the current index: After the popping is complete, push the current bar's index onto the stack.
- Handle remaining bars: After the loop, any indices left in the stack represent bars that have no smaller bar to their right. 
You can process them in the same way, with the right boundary being the end of the histogram.






"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i , h in enumerate(heights + [0]) :
            while stack and h < heights[stack[-1]]:
                height_index = stack.pop()
                height = heights[height_index]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area , height * width)
        
        return max_area
