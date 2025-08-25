"""
You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

Note:

The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.

# we can use the concept both pointers going to same direction 

We want to remove duplicates in-place using the same array, without creating a new one.
The idea is:

Use two pointers:
slow → marks the position of the last unique element.
fast → scans through the array to find the next different element.
Start with slow at index 0.
Move fast from left to right:
If nums[fast] == nums[slow], it’s a duplicate → skip it.
If nums[fast] != nums[slow], we’ve found a new unique element → place it at nums[slow + 1] and then move slow forward.
Continue until the end of the array.
The number of unique elements is slow + 1, and they occupy the first part of the array (nums[:slow+1]).
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0 
        fast = 1 
        n = len(nums)
        while fast < n :
            if nums[slow] != nums[fast] :
                nums[slow + 1] = nums[fast] 
                slow = slow + 1
            fast = fast + 1

        
        return slow + 1
