"""
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
Return the largest number of chunks we can make to sort the array.

The core idea is to find a split point i such that the maximum value in the subarray nums[0...i] is equal to i. If this condition holds, it means that all elements from 0 to i in the sorted version of the array are contained within the nums[0...i] subarray.

Here's the step-by-step approach:

Initialize a counter for chunks and a variable to track the maximum value seen so far.
Iterate through the array from left to right, maintaining the max_val of the subarray nums[0...i].
At each index i, if the max_val of the current subarray is equal to i, you have found a valid chunk. This is because all numbers from 0 to i must be present in nums[0...i] for it to be sorted independently, and if the maximum value is i, then no numbers larger than i are in the subarray. This means all the numbers from 0 to i are confined within that chunk.
Increment the chunk counter.
Repeat this process until you reach the end of the array. The final chunk count will be the maximum number of chunks possible.



"""


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        count = 0 
        max_till_now = 0 

        for index in range(len(arr)) :
            max_till_now = max(max_till_now , arr[index])
            if index == max_till_now :
                count += 1
            
        return count

"""
Max Chunks to make array sorted 2 :

You are given an integer array arr.
We need to split arr into the maximum number of chunks (i.e., partitions) such that, when each chunk is individually sorted and then concatenated, the result matches the sorted version of the entire array.

Return the largest number of chunks we can create to achieve this.

Input Format:
The first line contains an integer n, the length of the array arr.
The second line contains n space-separated integers representing the array arr.

Output Format:
Output a single integer, the largest number of chunks that can be created to sort the array.





Algorithm
Create a sorted copy: First, create a sorted copy of the input array, let's call it sorted_arr.
Initialize counters: Initialize two variables, chunks = 0, and prefix_sum = 0, and sorted_prefix_sum = 0.
Iterate and compare
Iterate through the array from i = 0 to n-1.
In each iteration, add arr[i] to prefix_sum and sorted_arr[i] to sorted_prefix_sum.
If prefix_sum is equal to sorted_prefix_sum, it means that the sum of elements in the prefix of the original array is equal to the sum of elements in the prefix of the sorted array. However, this is not a sufficient condition to guarantee that the sets of elements are the same. For example, [1, 2] has the same sum as [3, 0].
To handle duplicates and different arrangements, a more robust check is needed. A common method is to use a frequency map or, more efficiently, to track the sums of both the elements and their squares.
Let's use the sum approach for simplicity and effectiveness.
Initialize count_of_chunks = 0, sum1 = 0, and sum2 = 0.
Iterate from i = 0 to n-1:
sum1 += arr[i]
sum2 += sorted_arr[i]
If sum1 == sum2, it means we have a valid chunk.
Increment count_of_chunks.


The Fundamental Condition: A valid chunk boundary can be formed at index i if and only if the elements in the subarray arr[0...i] are exactly the same set of 
elements as those in sorted_arr[0...i], regardless of their order. For example, if arr[0...i] is [2, 1] and sorted_arr[0...i] is [1, 2], they contain the same 
elements, so a chunk boundary can be placed after the 1.

Why Sums Are Enough: Your immediate thought might be, "But two different sets of numbers can have the same sum, so how can a simple sum check be enough?" 
This is a great question. The reason it works is because of the specific nature of our sorted array. The prefix sorted_arr[0...i] is guaranteed to contain the 
smallest i+1 elements from the entire array. The sum of these i+1 smallest elements is unique.

The Proof: Let's say we have the prefix of the sorted array sorted_arr[0...i]. This set of numbers has a specific sum. If the prefix of the original array arr[0...i] has the exact same sum, it can only be because it contains the exact same set of numbers. It is impossible for arr[0...i] to have a different collection of numbers and still have the same sum as the set of the i+1 smallest numbers in the entire array. For instance, if arr[0...i] contained an element that was larger than some element in sorted_arr[0...i], it would have to contain an element that was smaller to balance the sum, which is impossible since sorted_arr[0...i] contains the smallest elements.


def solve():

    # Read the length of the array from standard input.
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print(0)
            return
        
        # Read the space-separated integers and convert to a list.
        arr_str = sys.stdin.readline().split()
        arr = [int(x) for x in arr_str]
    except (IOError, ValueError) as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        return
        
    # Create a sorted copy of the array.
    sorted_arr = sorted(arr)
    
    # Initialize variables to track cumulative sums and the number of chunks.
    chunks = 0
    sum_arr = 0
    sum_sorted_arr = 0
    
    # Iterate through the array to find valid chunk boundaries.
    for i in range(n):
        # Add the current element from both arrays to their respective sums.
        sum_arr += arr[i]
        sum_sorted_arr += sorted_arr[i]
        
        # If the cumulative sums are equal, it means the elements in the prefixes
        # are the same set (a valid chunk boundary exists).
        if sum_arr == sum_sorted_arr:
            chunks += 1
            
    # Print the final result.
    print(chunks)

if __name__ == "__main__":
    solve()


The Correct Algorithm
The fundamental principle for finding a valid chunk boundary at index i is that the maximum value in the left part of the array (arr[0...i]) must be less than or equal to the minimum value in the right part of the array (arr[i+1...n-1]).
Find Right Minimums: First, we pre-calculate an array, let's call it min_right, where min_right[i] stores the smallest value in the subarray arr[i...n-1]. We can do this efficiently by iterating backward from the end of the array.
Iterate and Check: We then iterate through the array from left to right, keeping track of max_left, the largest value encountered so far. At each index i, we check if max_left is less than or equal to min_right[i+1].
Count Chunks: If the condition holds, it means everything to the left of the current position is smaller than or equal to everything to the right, forming a valid chunk boundary. We increment our chunk count.
Final Count: The final answer is the number of valid boundaries we found plus one, to account for the last chunk.


"""


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        min_right = [0] * n 
        min_right[-1] = arr[n-1]

        for index in range(n - 2 , -1 , -1) :
            min_right[index] = min(arr[index] , min_right[index + 1])

        max_left = 0
        chunk = 0 
        for index in range(n - 1) : 
            max_left = max(arr[index] , max_left)

            if max_left <= min_right[index + 1]:
                chunk += 1
        
        return chunk + 1
