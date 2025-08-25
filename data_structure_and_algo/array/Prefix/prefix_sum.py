"""
A prefix sum, also known as a cumulative sum, is a simple but powerful technique used in computer science to quickly calculate the sum of elements 
within a specific range of an array. It involves creating a new array where each element stores the sum of all preceding elements up to that point in the 
original array. This allows for constant-time (O(1)) queries for the sum of any subarray, as opposed to the linear time (O(n)) required to calculate it on 
the fly.

How It Works
The process involves two main steps:

Prefix Sum Array Creation: You build a new array, let's call it prefixSumArray, from the original array, originalArray. The value at each index i in prefixSumArray is the sum of all elements from index 0 to i in originalArray.

Range Sum Query: Once the prefixSumArray is built, you can find the sum of any subarray from index i to j of originalArray by using a simple formula.

Step-by-Step Example

Let's use an example to illustrate. Suppose we have the following array:

originalArray = [2, 5, 8, 3, 6]

1. Creating the Prefix Sum Array

We'll build a new array, prefixSumArray, with the same number of elements.
prefixSumArray[0] = originalArray[0] = 2
prefixSumArray[1] = originalArray[0] + originalArray[1] = 2 + 5 = 7
prefixSumArray[2] = originalArray[0] + originalArray[1] + originalArray[2] = 2 + 5 + 8 = 15
prefixSumArray[3] = originalArray[0] + originalArray[1] + originalArray[2] + originalArray[3] = 2 + 5 + 8 + 3 = 18
prefixSumArray[4] = originalArray[0] + originalArray[1] + originalArray[2] + originalArray[3] + originalArray[4] = 2 + 5 + 8 + 3 + 6 = 24
The resulting prefixSumArray is: [2, 7, 15, 18, 24]

Notice a pattern: prefixSumArray[i] can be calculated as prefixSumArray[i-1] + originalArray[i]. This makes the creation process a single linear pass (O(n)) through the array.

2. Performing Range Sum Queries

Now, let's say we want to find the sum of the elements in originalArray from index 1 to 3 (i.e., 5 + 8 + 3). The naive way is to loop and add them up, which takes O(n) time.
Using the prefix sum array, we can use the following formula:
Sum(i, j) = prefixSumArray[j] - prefixSumArray[i-1]
P[i-1] is to remove the sum of all elements that come before the start of our desired range. Let's break this down
P[i-1] is the sum of all elements from index 0 up to and including index i-1.
P[j] is the sum of all elements from index 0 up to and including index
i is the starting index of the range.
j is the ending index of the range.
For our example, i=1 and j=3.
prefixSumArray[3] = 18
prefixSumArray[1-1] = prefixSumArray[0] = 2
So, Sum(1, 3) = 18 - 2 = 16.

Let's double-check the sum from the original array: 5 + 8 + 3 = 16. The formula works!
Handling Edge Cases

A special case arises when the range starts at index 0 (i.e., i=0). In this scenario, the formula prefixSumArray[j] - prefixSumArray[i-1] would try to access an invalid index (-1). To handle this, we simply state that the sum of a range starting at 0 is simply prefixSumArray[j]. A common implementation practice is to pad the prefixSumArray with a 0 at the beginning.

paddedPrefixSumArray = [0, 2, 7, 15, 18, 24]
Now, the formula becomes: Sum(i, j) = paddedPrefixSumArray[j+1] - paddedPrefixSumArray[i]
Using this formula for our example (i=1, j=3):
paddedPrefixSumArray[3+1] = paddedPrefixSumArray[4] = 18
paddedPrefixSumArray[1] = 2

Sum = 18 - 2 = 16. The result is the same, and this version handles the i=0 case gracefully.

Time and Space Complexity
Time Complexity:

Prefix Sum Array Creation: O(n), as you need to iterate through the original array once.

Range Sum Query: O(1), as you only need to perform a single subtraction operation.

Space Complexity:

O(n), as you need to store the prefix sum array, which is the same size as the original array.

Applications
The prefix sum technique is a fundamental building block for many algorithms and is particularly useful in competitive programming and data analysis. Some common applications include:

Finding the sum of a subarray: This is the most direct application.
Solving problems on 2D arrays (Prefix Sum Matrix): The concept can be extended to two dimensions to find the sum of any sub-rectangle in a matrix.
Sliding window problems: Optimizing problems that involve finding a maximum or minimum sum in a window of a fixed size.
Dynamic programming: Used as a pre-computation step in certain DP problems.


Common Questions
Finding Subarray Sums:

Question: Given an array of integers, find the sum of elements within a given range [i, j].

Prefix Sum Application: You build a prefix sum array in O(n) time. After that, each query for a range sum takes O(1) time. This is the most direct application.

Finding a Subarray with a Specific Sum:

Question: Find if there exists a subarray with a given target sum k.

Prefix Sum Application: You can iterate through the prefix sum array. For each element P[i], you check if a previous prefix sum P[j] exists such that P[i] - P[j] = k. This is often done using a hash map to store previously seen prefix sums, allowing for an O(n) solution.

Maximum Subarray Sum (Kadane's Algorithm):

Question: Find the contiguous subarray within a one-dimensional array of numbers that has the largest sum.

Prefix Sum Application (variation): While Kadane's algorithm is the standard O(n) solution, you can also solve this with prefix sums. The maximum subarray sum is the maximum value of P[j] - P[i] where j > i. This can be optimized by keeping track of the minimum prefix sum encountered so far as you iterate, leading to an O(n) solution.

Variations and Extensions

Prefix Sum on 2D Arrays (2D Prefix Sum/Summed-Area Table):
Question: Given a 2D matrix, find the sum of elements within a given rectangular sub-grid.
Prefix Sum Application: You build a 2D prefix sum matrix where each cell P[i][j] stores the sum of all elements in the rectangle from (0, 0) to (i, j) in the original matrix. A query for the sum of any sub-rectangle can then be answered in O(1) time using a formula involving four lookups.

Difference Array / Range Updates:
Question: Given an array, perform multiple updates where a constant value is added to a range of elements.
Prefix Sum Application: Instead of updating the array directly, you create a "difference array." To add a value x to a range [i, j], you simply add x at index i and subtract x at index j+1 in the difference array. After all updates are done, you calculate the prefix sum of the difference array. The resulting array is the final updated array. This is efficient for a large number of range updates.

Binary Indexed Tree (Fenwick Tree) and Segment Tree:
Question: Given an array, perform both range sum queries and single-element updates efficiently.
Prefix Sum Application (enhancement): The basic prefix sum technique is not efficient for updates (O(n) per update). Data structures like Binary Indexed Trees and Segment Trees are advanced variations that build on the prefix sum concept. They allow for both range sum queries and point updates in O(logn) time.

Handling Negative Numbers:
Question: Find the number of subarrays with a specific sum k in an array that can contain negative numbers.
Prefix Sum Application: This is a classic prefix sum problem. You use a hash map to store the frequency of each prefix sum encountered. For each new prefix sum P[i], you check if P[i] - k exists in your hash map. The number of times it exists is the number of subarrays ending at i with sum k.


"""


def prefix_sum(arr) :
    if not arr:
        return []

    n = len(arr)
    prefix_sum = [0] * n 
    prefix_sum[0] = arr[0]

    for index in range(1 , n) :
        prefix_sum[index]  = prefix_sum[index - 1] + arr[index] 

    return prefix_sum

# arr = [1 , 2 , 3 , 4 ,5]
# print(prefix_sum(arr))


"""
You are given an array ‘arr’ of size ‘N’. You are provided with ‘Q’ queries, each containing two integers, 
‘L’ and ‘R’. Your task is to return the sum of elements from the position ‘L’ to ‘R’ for each query.

For example:
You are given arr = [1, 3, 4, 5, 6, 9], and queries = [[1, 3], [5, 6] , [1, 6]].
For the first query [1, 3] sum of elements = 1 + 3 + 4 = 8. Hence the answer is 8
For the second query [5, 6] sum of elements = 6 + 9 = 15. Hence the answer is 15
For the third query [1, 6] sum of elements = 1 + 3 + 4 + 5 + 6 + 9= 28. Hence the answer is 28. 
Hence the final answer is [8, 15, 28]


"""

def sum_range_query(arr , q) :
    result = []

    prefix_sum_arry = prefix_sum(arr)

    for query in q :
        L = query[0]
        R = query[1]

        if L == 0 :
            range_sum  = prefix_sum_arry[R]
        else:
            range_sum  = prefix_sum_arry[R] - prefix_sum_arry[L - 1]
        
        result.append(range_sum)
    
    return result

arr = [1, 3, 4, 5, 6, 9]
queries = [[1, 3], [5, 6] , [1, 6]]

print(sum_range_query(arr , queries))


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    
    def prefixSum(self,A):
        n = len(A)
        result = [0] * n
        result[0] = A[0]

        for index in range(1 , n):
            result[index] = result[index - 1] + A[index]
        
        return result

    def rangeSum(self, A, B):
        prefixSum_arr = self.prefixSum(A)
        result = list()

        for query in B :
            L = query[0]
            R = query[1]

            if L == 0 :
                total = prefixSum_arr[R]
                result.append(total)
            else :
                total = prefixSum_arr[R] - prefixSum_arr[L - 1]
                result.append(total)
        

        return result
