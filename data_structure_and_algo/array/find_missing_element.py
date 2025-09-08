"""
Find Missing Element :

Approaches to Find the Missing Element
1) XOR Approach

Iterate through numbers from 1 to n+1 and compute their XOR (xor_range).
Compute XOR of all elements in the given array (xor_array).
Since duplicates cancel out in XOR, the result xor_range ^ xor_array will give the missing element.

2) Sum Approach

Compute the sum of all numbers from 1 to n+1 (using formula or loop).
Compute the sum of all elements in the array.
The difference (sum_of_range – sum_of_array) is the missing element.

3) Auxiliary Space Approach

Create a boolean/marker array of size n+1.
For each element x in the array, mark its position (marker[x] = 1).
Traverse the marker array: the index with value 0 corresponds to the missing number.

4) Sorting Approach

Sort the given array.
Traverse numbers from 1 to n+1.
Compare with the array elements in order; the first mismatch gives the missing number.

5) Swapping / Cyclic Sort Approach

Place each number in its correct index position (x should be at index x-1).
After all elements are placed correctly, traverse the array:
If arr[i] != i+1, then i+1 is the missing element.

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0 
        n = len(nums) 

        for i in range(1 , n + 1) :
            result = result ^ i 
        
        for num in nums :
            result = result ^ num
             
        return result



class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0

        # Phase 1: Place each number in its correct position using cyclic sort
        while i < n:
            correct_index = nums[i]
            
            # The condition 'correct_index < n' handles the missing number 'n'
            if correct_index < n and nums[i] != nums[correct_index]:
                # Swap the number to its correct position
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                # If the number is already in place or out of range, move to the next index
                i += 1

        # Phase 2: Find the first missing number by iterating through the sorted array
        for i in range(n):
            if nums[i] != i:
                return i

        # If the loop completes, it means the numbers 0 to n-1 are present,
        # so the missing number is n.
        return n
    

"""

1. Using a Hash Map (Dictionary)
This is the most flexible and generally best method for finding all repeating elements, especially when you need to know their frequencies.

How It Works: You iterate through the list and use a hash map (dictionary in Python) to store each element and its count. If an element is already in the map, you increment its count; otherwise, you add it with a count of 1.

Pros:

Versatile: Works for any data type (strings, numbers, etc.).

Time Complexity: O(n), as you iterate through the list once to build the map and once more to find the repeating elements.

Space Complexity: O(k), where 'k' is the number of unique elements, which in the worst case can be O(n).

Example: To find repeating numbers in [1, 2, 3, 2, 4, 1, 5]:

Initialize counts = {}.

Iterate and populate counts: {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}.

Iterate through counts and find elements with a count greater than 1: [1, 2].

2. Sorting the Array
This method is efficient if you can modify the original array or don't mind the time cost of sorting.

How It Works: Sort the array first. This brings all identical elements together. Then, iterate through the sorted array and find adjacent elements that are the same.

Pros:

Simple Logic: The concept is easy to understand and implement.

Space Complexity: O(1) if sorting is done in-place (though some sorting algorithms like Merge Sort require O(n) space).

Cons:

Time Complexity: O(n log n) due to the sorting step. This is slower than using a hash map for large datasets.

Data Type Limitation: Requires a data type that is sortable.

Example: For [1, 2, 3, 2, 4, 1, 5]:

Sort the array: [1, 1, 2, 2, 3, 4, 5].

Iterate and find duplicates: The first 1 is a duplicate because the next element is also 1. The first 2 is a duplicate because the next element is 2.


"""

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        result =  i  = 0


        while i < n :
            if nums[i] <= 0 or nums[i] > n :
                i = i + 1
                continue 
            
            index = nums[i] - 1
            if nums[i] != nums[index] :
                nums[i] , nums[index] = nums[index] , nums[i]
            else :
                i = i + 1
        
        for i in range(n) :
            if nums[i] != i + 1:
                return i + 1

        return n + 1
