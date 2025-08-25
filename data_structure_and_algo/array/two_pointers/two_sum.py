"""
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O(1)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]



Here array is sorted 
so we are using two pointer approch with opposite direction 
array is sorted 
it just reduce search space overall make overall code time complexity to 0(n) we are just reducing overall search space 
suppos we start with left and right where left represent first and right represent last element 

if nums[left] + nums[right]  == k : means we found the solution so we can directly add to result and return 

if nums[left] + nums[right] < k :  adding first and last element still resultent value is small as compared to target  so we need to move left pointer to make value bigger

if nums[left] + nums[right] > k : so sum of both we forming the large value even if you are moving left it will not make send it will form even larger value so we need to decrease the right value which might make result smaller 
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []