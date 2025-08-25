"""
Step 1: Sort the Array
Just like with 3-sum, the first and most critical step is to sort the input array. Let's call our array nums. Sorting nums allows us to use the two-pointer technique and easily handle duplicate elements. The time complexity for this step is O(nlogn).

Step 2: Iterate with Two Nested Loops
After sorting, we'll use two nested loops to fix the first two numbers of our quadruplet. Let's call the pointers for these loops i and j.

The outermost loop, with pointer i, will iterate from the beginning of the array up to the fourth-to-last element.

The inner loop, with pointer j, will start from i + 1 and go up to the third-to-last element.

Inside these loops, nums[i] and nums[j] are the first two numbers of our potential quadruplet. We now need to find two more numbers, c and d, such that nums[i] + nums[j] + c + d = target.

To simplify, let's define a new target for the remaining two numbers: new_target = target - nums[i] - nums[j]. We now need to find two numbers, c and d, that sum up to new_target. This is a classic 2-sum problem!

Step 3: Use the Two-Pointers Technique for 2-Sum
To find the remaining two numbers, we'll use the two-pointer approach within the nested loops.

Initialize a left pointer L at j + 1.

Initialize a right pointer R at the end of the array.

We'll use a while loop where L is less than R to find the two numbers.

Calculate the current sum of the two pointers: current_sum = nums[L] + nums[R].

If current_sum is equal to new_target, we have found a valid quadruplet: [nums[i], nums[j], nums[L], nums[R]]. Add this quadruplet to our result list. Then, to find other potential unique quadruplets, we move both pointers inward by incrementing L and decrementing R. To avoid duplicate quadruplets, we must skip any duplicate numbers at the L and R pointers. We increment L as long as it points to the same number as the previous one, and do the same for R by decrementing it.

If current_sum is less than new_target, it means our sum is too small. To make it larger, we must increase the left number, so we increment L.

If current_sum is greater than new_target, our sum is too large. To make it smaller, we must decrease the right number, so we decrement R.

Step 4: Handle Duplicates
Handling duplicates is crucial to ensure the final result contains only unique quadruplets. Since the array is sorted, duplicate numbers will be adjacent.

The outermost loop (for i) should check if the current element is the same as the previous one. If nums[i] == nums[i-1], skip the iteration to avoid redundant calculations.

The second loop (for j) should also check if nums[j] == nums[j-1] and skip the iteration if they are the same.

Inside the two-pointer while loop, after finding a valid quadruplet, we must advance the pointers past any duplicates. For L, we increment it as long as L < R and nums[L] == nums[L-1]. For R, we decrement it as long as L < R and nums[R] == nums[R+1].

The overall time complexity is dominated by the two nested loops and the inner two-pointer pass, resulting in O(n 
3
 ). While this is not as efficient as the O(n 
2
 ) 3-sum solution, it is the most optimal approach for the 4-sum problem.

An image of the four sum algorithm would provide a good visual aid .









"""

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if total_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result
