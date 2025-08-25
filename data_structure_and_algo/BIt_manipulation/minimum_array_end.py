"""
📌 Problem Statement Summary
You are given:
An integer n – size of the array
An integer x – the result of the bitwise AND of all array elements
You must construct an array nums[] of size n where:
nums[i + 1] > nums[i] for all 0 <= i < n - 1 (strictly increasing)
nums[0] & nums[1] & ... & nums[n - 1] == x
All elements are positive integers
Return the minimum possible value of nums[n - 1].


Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

"""