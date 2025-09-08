class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        left = 0 
        result = 0 

        for right in range(n) :
            if nums[right] == 0 :
                k -= 1
            
            while k < 0 :
                if nums[left] == 0 :
                    k = k + 1
                left = left + 1
            result = max(result , right - left + 1)
        
        return result


"""
Just use sliding window dynamic with 
"""