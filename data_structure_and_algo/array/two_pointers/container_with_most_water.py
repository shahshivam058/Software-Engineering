"""
Container With Most Water - Explanation
Problem Link

Description
You are given an integer array heights where heights[i] represents the height of the 
i th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

an array of heights using hieght most water we can using left height and right height 

using left and right height max water we can save 

easiest way to try all combinations 

try each and every single combination 

between 2 height there will be space identidy max water we can save 


height can be smallest of left and right bar * distance between right and left (min(a[l] , a[r]) * (r - l))

we are taking minimum height as we cant store water more than minimum height 

we can try all brute force approch  and identify the maximum result 


2 pointer 

Two-Pointer Approach Explained
The two-pointer approach is an efficient way to solve this problem with a time complexity of O(n). It works as follows:

Initialization: Start with two pointers, one at the beginning of the array (left) and one at the end (right).

left = 0
right = n - 1
max_area = 0
Calculation Loop: Iterate while the left pointer is less than the right pointer. In each iteration, calculate the current area and update the max_area.

The width is the distance between the two pointers: right - left.

The height is the minimum of the two heights: min(height[left], height[right]).

The area is width * height.

Move Pointers: This is the most crucial step. To find a potentially larger area, we must move one of the pointers. Since the width is guaranteed to decrease with each step, the only way to get a larger area is by finding a container with a greater height. To maximize the chance of this, we always move the pointer of the shorter line inward.

If height[left] < height[right], increment left.

If height[right] <= height[left], decrement right.

The reason we move the shorter pointer is because moving the taller one would not lead to a better result. 
For example, if height[left] is shorter, moving left to left + 1 might give us a taller line that can form a larger container with right. 
However, if we were to move right instead, the new height would be limited by the shorter height[left] and the width would be smaller,
 making it impossible to get a larger area. By following this strategy, we effectively eliminate suboptimal solutions and guarantee that we will find the optimal one.




"""

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res