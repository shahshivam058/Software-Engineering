"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].




sort the input array 



This question is nothing but extension of 2 sum 

we want 3 number of array and sum to be 0 
we cant have duplicate in solution 
so we can Brute force solution is nothing but try all possibality of all 3 elements 



once we know first number we can use 2 sum approch 


Optimal approch 


Sort the array 
we need combination of 3 digits 
we can get first digit by looping over array 
other 2 digits we can get through the applying 2 sum logic 




"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n): # first digit from array we need to find remaining 2 in array 
            
            if i > 0 and nums[i] == nums[i-1] : # check if num  valid or index or number same as previous one 
                continue 
            
            # insilize the pointers
            left = i+1 
            right = n - 1

            while left < right : # run 2 sum approch just add logic to skip duplicates 
                total = nums[i] + nums[left] + nums[right]
                if total == 0 :
                    result.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    
                    # we dont want to do 
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                        
                    left = left + 1
                    right = right - 1

                elif total < 0 :
                    left = left + 1 
                else:
                    right = right - 1

        return result


"""
Step 1: Sort the Array
First, sort the input array in non-decreasing order. This is a crucial step that enables the two-pointer technique. Let's say our array is nums. After sorting, we get a new array, say sorted_nums.
The time complexity of sorting is typically O(nlogn), which is more efficient than the O(n 
3
 ) brute-force method.

Step 2: Iterate and Use Two Pointers
After sorting, iterate through the array with a single pointer, let's call it i, from the beginning up to the third-to-last element. This pointer will represent our first number, a.
For each i, we need to find two other numbers, b and c, such that a+b+c=0. This simplifies to b+c=−a.

To find these two numbers, we use two more pointers:

A left pointer L, initialized to i + 1. This pointer will represent our second number, b.

A right pointer R, initialized to the end of the array. This pointer will represent our third number, c.

Step 3: Move the Pointers
Now, inside the loop for i, we enter a while loop where L is less than R. In each iteration of this inner loop, we calculate the current sum: current_sum = nums[i] + nums[L] + nums[R].

If current_sum is equal to zero, we have found a valid triplet [nums[i],nums[L],nums[R]]. We add this triplet to our result list. Then, to find other unique triplets, we need to move both L and R. We increment L and decrement R. To avoid duplicate triplets, we also need to skip any duplicate numbers at the L and R pointers. We continue to increment L as long as nums[L] is the same as the previous nums[L], and similarly for R.

If current_sum is less than zero, it means our sum is too small. To make it larger, we need to increase the value of b (our second number). We do this by incrementing the left pointer L.

If current_sum is greater than zero, our sum is too large. We need to decrease the value of c (our third number). We do this by decrementing the right pointer R.

Step 4: Handle Duplicates
To ensure that the triplets in our result are unique, we must handle duplicate values. Since the array is sorted, duplicate numbers will be adjacent.

The outer loop for i should check if the current element is the same as the previous one. If nums[i] == nums[i-1], we should skip this iteration to avoid considering the same a value again.

Inside the while loop for the two pointers, after finding a valid triplet and moving the pointers, we need to skip over any duplicate values for b and c. We increment L as long as L < R and nums[L] == nums[L-1]. Similarly, we decrement R as long as L < R and nums[R] == nums[R+1].



"""