from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low , mid , high = 0 , 0 , len(nums) - 1

        while mid <= high :
            if nums[mid] == 1:
                mid = mid + 1
            elif nums[mid] == 0 :
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low = low + 1
                mid = mid + 1
            else :
                nums[mid] , nums[high] = nums[high]  , nums[mid]
                high = high - 1
        
        return nums
    
"""
The Approach: The Three-Pointer Technique
The algorithm uses three pointers, which act as boundaries for the different sections of the array.

low: This pointer marks the boundary for the "red" (smallest) section. Everything to its left is a 0. It starts at the beginning of the array.

mid: This is the current element being examined. It traverses the array from left to right.

high: This pointer marks the boundary for the "blue" (largest) section. Everything to its right is a 2. It starts at the end of the array.

The Core Logic
The algorithm iterates using the mid pointer from the start of the array until it crosses the high pointer. At each step, it checks the value of the element at arr[mid] and performs one of three actions:
If arr[mid] is a 0 (red): This element belongs in the first partition. We swap it with the element at arr[low] to move it to the beginning. Since we've placed a 0 correctly and the element at low is either a 0 or 1 (which is in the correct section), we can safely increment both low and mid.
If arr[mid] is a 1 (white): This element is already in the correct middle partition. There's no need to swap. We simply increment mid to move to the next element.
If arr[mid] is a 2 (blue): This element belongs in the last partition. We swap it with the element at arr[high]. Since the 2 is now in its correct final position, we decrement high. We don't increment mid because the element that was swapped from the high position is now at mid, and its value is unknown (it could be a 0, 1, or 2), so it must be checked in the next iteration.
This process ensures that as mid moves through the array, the three partitions grow and the unsorted section in the middle shrinks. When mid eventually surpasses high, the array is completely sorted. 🚩
"""