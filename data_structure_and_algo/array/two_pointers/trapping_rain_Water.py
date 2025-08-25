"""

The Core Idea

For any given bar at index i, the amount of water it can trap is determined by the height of the tallest bar to its left and the tallest bar to its right. 
The water level at this position will be the minimum of these two maximum heights. The amount of water trapped above the current bar is then calculated as:

Brute force : for each element search on left and search on right max and calculate

Trapped Water = min(max_height_left, max_height_right) - current_height

To find the total trapped water, we sum this value for every bar in the array.

The Prefix and Suffix Sum Approach
This method uses two auxiliary arrays to pre-compute the maximum heights, allowing us to find the water level for each position in O(1) time.

1. The Prefix Array (Left Maxes)
First, we create a prefix array (let's call it left_max) to store the tallest bar encountered so far from the left side. We iterate through the input array from left to right. At each index i, left_max[i] will store the maximum height seen up to and including index i.

Initialization: left_max[0] = height[0]

Iteration: left_max[i] = max(left_max[i-1], height[i]) for i > 0

For example, if the heights are [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], the left_max array would be:

[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

2. The Suffix Array (Right Maxes)
Next, we create a suffix array (let's call it right_max) to store the tallest bar encountered so far from the right side. We iterate through the input array from right to left. At each index i, right_max[i] will store the maximum height seen from the end of the array up to and including index i.

Initialization: right_max[n-1] = height[n-1]

Iteration: right_max[i] = max(right_max[i+1], height[i]) for i < n-1

Using the same example [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], the right_max array would be:

[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]

3. Calculating Trapped Water
Finally, we iterate through the input array a third time, from left to right. For each position i, we calculate the water trapped at that spot using the pre-computed left_max and right_max arrays.

For each i:

The water level is water_level = min(left_max[i], right_max[i]).

The water trapped at this position is water_level - height[i].

We add this value to a running total.




How the Logic Works Step-by-Step
The two-pointer method avoids creating auxiliary arrays by simultaneously tracking the maximum heights from both the left and right.
Initialize Pointers and Maxima: You start with a left pointer at the beginning of the array and a right pointer at the end. You also maintain left_max and right_max variables, initialized to 0. These variables will store the highest bar encountered so far from each direction. 💧
Move the Shorter Pointer: In each step of the loop, you compare the heights at the left and right pointers.
If height[left] <= height[right]: The height of the left wall is the limiting factor. The amount of water that can be trapped at the current left position is determined by the left_max. You calculate this (left_max - height[left]), add it to the total, and then move the left pointer to the right. You update left_max to the maximum of its current value and the new height[left].
If height[left] > height[right]: The height of the right wall is the limiting factor. The amount of water trapped at the current right position is determined by the right_max. You calculate the water for this position (right_max - height[right]), add it to the total, and then move the right pointer to the left. You update right_max to the maximum of its current value and the new height[right].
The Guarantee: This logic works because when you choose to move a pointer, you are making a commitment. For example, when you move the left pointer, you are saying that height[right] is tall enough to contain any water up to the left_max for the current left position. This is a valid assumption because height[right] is already greater than or equal to height[left]. You can confidently calculate the trapped water at the left pointer based only on left_max without needing to know the maximum height of the entire right side of the array. The same logic applies when moving the right pointer.




"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res


def trap(height):
    """
    Calculates the total amount of rainwater that can be trapped.

    This function uses a two-pointer approach that traverses the array from
    both ends simultaneously. It maintains the maximum height seen from the
    left and right sides and calculates the trapped water at each step based
    on the shorter of the two boundary walls. This approach has an O(1) space
    complexity, making it highly efficient.

    Args:
        height (list[int]): A list of non-negative integers representing the
                            height of each bar.

    Returns:
        int: The total amount of trapped rainwater.
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left < right:
        # Check which side is the shorter wall and is limiting the water level.
        if height[left] < height[right]:
            # The left side is the shorter wall.
            # Update the left_max.
            if height[left] > left_max:
                left_max = height[left]
            else:
                # Calculate trapped water at the current left position.
                total_water += left_max - height[left]
            # Move the left pointer inward.
            left += 1
        else:
            # The right side is the shorter or equal wall.
            # Update the right_max.
            if height[right] > right_max:
                right_max = height[right]
            else:
                # Calculate trapped water at the current right position.
                total_water += right_max - height[right]
            # Move the right pointer inward.
            right -= 1

    return total_water


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
