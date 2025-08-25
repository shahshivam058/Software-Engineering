"""
Sorted array nums
all numbers are non negative 
and int maximum bit 
you want to perform following query 2 time 

Find a non-negative integer k < 2 ** maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.
we want anwser in form of query 
do xor for each all elemts with some int k such that it can not be greter than 2 ^ max bits

starting from first to last element everytime while doing xor avoid doing n - loop 
optimal k 


💡 Problem Summary
You're given:

A sorted array nums of non-negative integers.

An integer maximumBit.

You must perform n queries (where n = len(nums)). In each query:

Compute the XOR of all elements in the current nums.

Find a k (where 0 ≤ k < 2^maximumBit) that maximizes (XOR of nums) ^ k.

Return k for this query.

Remove the last element of nums.

Repeat until nums is empty.



"""

class Solution:
    def getMaximumXor(self, nums, maximumBit):
        n = len(nums)
        answer = [0] * n
        xorSum = 0
        
        # Precompute total XOR of all elements
        for num in nums:
            xorSum ^= num
        
        maxVal = (1 << maximumBit) - 1  # This is 2^maximumBit - 1
        
        for i in range(n):
            # Best k is the one that maximizes xorSum ^ k → flip all bits
            answer[i] = xorSum ^ maxVal
            
            # Remove last element from XOR (simulate removing from nums)
            xorSum ^= nums[n - 1 - i]
        
        return answer
    

class Solution:
    def getMaximumXor(self, nums, maximumBit):
        n = len(nums)
        xorsum = 0
        maxval = (1 << maximumBit) - 1
        res = []

        for num in nums:
            xorsum ^= num
            res.append(xorsum ^ maxval)

        return res[::-1]
