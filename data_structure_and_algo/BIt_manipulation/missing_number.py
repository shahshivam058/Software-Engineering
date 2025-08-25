class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0 
        n = len(nums)
        for number in range(n+1) :
            result = result ^ number
        
        for number in nums :
            result = result ^ number
        
        return result 


"""
Here the main aim is our array is from 0 to n and size of array is n - 1 one elements is missing findout 

# we can do sum of all elements from 0 to n lets assume it a and sum of all elements from array assume b do a - b 
# we can do very similer approch as above but with xor do xor of all elements from 0 to n and do xor of all elements from array duplicate number will be cancell it self
"""