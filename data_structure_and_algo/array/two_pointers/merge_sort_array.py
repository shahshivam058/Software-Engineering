"""
You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:

m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

Example 1:

Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

Output: [1,2,10,20,20,40]
Example 2:

Input: nums1 = [0,0], m = 0, nums2 = [1,2], n = 2

Output: [1,2]

brute force :

create a new array merge both 
sort 
time complexity is o(n) but extra memory 



Optimal 

rather than going forward go backward it will be easy 


Insilize pointer at last element in array nums1
we want largest value at the end of array last index in nums1
start at last real value in num 1 and last real value in nums2 
compare both and greter value place at last element in nums1 last index 
do same with last real and last real in nums2 
place greter element in nums1 2nd last index and 
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1  # represents last index in nums1

        # Merge in reverse order
        while m > 0 and n > 0: # merge in reverse order come backwards 
            if nums1[m - 1] > nums2[n - 1]: # check last real element in nums1 with last real element in nums2 what ever is bigger will be placed in last index in array and decrease backwards
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1 

        # Fill nums1 with leftover nums2 elements
        while n > 0: # if nums2 still has element that are left then nums1 with leftover nums2 elements
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1