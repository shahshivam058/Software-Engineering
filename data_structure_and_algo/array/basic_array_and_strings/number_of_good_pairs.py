"""
Leetcode Link : https://leetcode.com/problems/number-of-good-pairs/

Brute force approch : we can use nested loops and compare all the posible pairs and  count all possible pairs returns 
Better solution : we have  same digit multiple time where it is doesnt metter 
                  we can just count how many time each number oocure 
                  calculate the number of possible pairs 
                  suppos if we have 4 times 1 how many possiblel pairs it will make 
                   1 1 1 1 
                   3 with first 1 
                   2 with  2nd one 
                   1 with 3rd one 
                   we can just use the comman formula 
                   c * (c - 1 )// 2
                   if count is even 1 math wil work out 

                   we can create a dict store the number and frequency againest that number 
                   for each number use the formula using freq count the number of possible pairs and add it to result 
optimal solution : we are just calculeting the result while counting the freq we are not gona do after that 
                   count the result while  processing 
                   we just need to check if number already available in hashmap or not if available it forms pair add it to result 
                   res += count[num]: if num has been seen before k times, then this current number can form k good pairs with the previous occurrences. So we add k to the result.
                    Then, we increase count[num] by 1 because we've now seen this number one more time.

                    without defaultdict :
                    just add to dict with count if first time with freq 1 if already available in hashmap add freq to result and increase the count 


"""

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for num, c in count.items():
            res += c * (c - 1) // 2
        return res
    

from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        res = 0
        for num in nums:
            if num in count:
                res += count[num]
                count[num] += 1
            else:
                count[num] = 1
        return res
