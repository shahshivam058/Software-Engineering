"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 size of window should be <= k 

 if both start and end point to first element then window size is 1 

 find a valid windod of size k + 1 

 here window is taken by end - start index 

 hashset or hashmap is something we can use 

 we can use sliding window 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false



Let's clarify the difference between the two concepts:

Window size (Number of elements): This is the count of elements currently in your data structure (e.g., a set or a list). In a fixed-size sliding window, this count is always constant. In a dynamic-size window, it changes. For "Contains Duplicate II," you'll only ever have at most k+1 elements in your set.

Distance (Index difference): The problem's constraint abs(i - j) <= k is about the distance between indices. If you're at index i, any potential duplicate j must be in the range i - k <= j < i. This means you're checking against a "look-back" window of size k.




The Sliding Window Approach
A sliding window is the most efficient way to solve this problem. The core idea is to maintain a set of numbers that are within the current window of size k. As you iterate through the array, you perform two main actions:

Add the current number to the window: For each number nums[i], you check if it's already in your set. If it is, you've found a duplicate within a distance of k and can immediately return True. If it's not, you add it to the set.

Slide the window by one: As you move from index i to i + 1, the element at index i - k is now outside the window of size k. You must remove this element from your set to keep the window's contents accurate.



"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        window = set()

        for i in range(n) :
            if nums[i]  in window :
                return True
            
            window.add(nums[i])

            if len(window) > k :
                element_to_remove = nums[i - k]
                window.remove(element_to_remove)

        
        return False