from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start_window = 0 
        total_sum = 0
        n = len(nums) 
        window_size = float("inf")

        for end_window in range(n) :
            total_sum = total_sum + nums[end_window] 

            while total_sum >= target :
                window_size = min(window_size , end_window - start_window + 1)
                total_sum -= nums[start_window]
                start_window += 1


        return 0 if window_size == float("inf") else window_size     



