"""
Description
The next greater element of some element x in an array is the first greater element that is to the right of x in the array.
You are given two 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. nums2 contains unique elements.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.


for element in nums1 found in nums2 and check if any greter element available on right if yes return that else return -1 

solution 

create a hashmap storing value - > index 

Now Loop Through nums2 check if number available in nums1
check for next greter element for it in array and store it in result array 
im result it should be on same index as index in main nums 1 
insilizr array with - 1

o (n ** 2)

we are creating hashmap to keep track of index on which index particular value is so we can add it to result array
create a result array same as size of nums1

use the monotonic stack concept 
identify the current element 
if stack has element then check if last value in stack less then current element if yes then 
pop the element from stack store popped value 
get the index from hashmap 
store in result at particular index

and add only in stack if its in nums1

"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
    

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res