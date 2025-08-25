Kadane’s algorithm finds the maximum subarray sum of a 1-D array in O(n) time and O(1) space. It’s the gold standard for problems like “largest sum of contiguous elements.”

What problem does it solve?

Given an array a[0..n-1] (can contain negatives), find

max over 0 ≤ L ≤ R < n of  a[L] + a[L+1] + … + a[R]


Core idea (intuition)

While scanning left to right, maintain:

cur: the best suffix sum ending at the current index (i.e., maximum sum of any subarray that must end here).
best: the best overall subarray sum seen so far.

If your current suffix sum ever becomes negative, it can only hurt any future subarray you try to extend (adding a negative prefix drags down future sums). 
So you “drop” it and restart at the next element.

That’s it. Keep the best suffix sum; reset when it’s negative.


Formal invariant (why it works)

At index i (0-based):

cur = max over all L ≤ i of a[L] + … + a[i]
(best subarray that ends exactly at i)

best = max over all 0 ≤ L ≤ R ≤ i of a[L] + … + a[R]
(best seen anywhere up to i)


cur = max(a[i], cur + a[i])     // either start fresh at i, or extend
best = max(best, cur)


Common edge cases & choices

All numbers negative

Standard Kadane (as above) returns the largest element (e.g., array [-5,-2,-7] → -2).

If your specification allows the empty subarray, you might want result 0. Then use:

cur = 0; best = 0
for x in a:
    cur = max(0, cur + x)
    best = max(best, cur)


But note: this version loses indices and treats all-negative arrays as 0.

Indices retrieval

Track tempStart when you reset cur. Whenever best improves, set (start, end) = (tempStart, i).

Overflow/large sums

Use 64-bit integers if the input can be large (long long in C++, long in Java; Python is safe).

Empty array input

Define behavior: often throw/return sentinel (or 0 if empty-allowed variant).

Streaming data

Kadane is online: you can process items as they arrive without storing the whole array.


Time and Space Complexity
Time Complexity: O(n) ⏱️
The algorithm iterates through the array just once, making its time complexity linear with respect to the number of elements in the array. This is extremely efficient.

Space Complexity: O(1) 💾
The algorithm only uses a few variables to store the current and global maximums. It doesn't require any extra data structures, so its space complexity is constant.





def kadane_algorithm(nums):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's algorithm.

    Args:
        nums: A list of numbers.

    Returns:
        The maximum sum of a contiguous subarray.
    """
    if not nums:
        return 0

    current_max = 0
    global_max = nums[0]

    for x in nums:
        # Add the current element to the current_max
        current_max += x
        
        # Update global_max if current_max is greater
        if current_max > global_max:
            global_max = current_max
        
        # If current_max becomes negative, reset it to 0
        # This is the key step to start a new subarray
        if current_max < 0:
            current_max = 0

    return global_max

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = kadane_algorithm(arr)
print(f"The maximum contiguous sum is: {max_sum}")  # Output: The maximum contiguous sum is: 6



1. Basic Problem
Maximum Sum Subarray: This is the core problem that the algorithm was designed for. Given an array of numbers, find the contiguous subarray with the largest sum.

Example: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ] -> The maximum sum is 6 (from [4, -1, 2, 1]).

2. Variations on the Basic Problem
Finding the Subarray Itself: Instead of just returning the maximum sum, a variation is to return the start and end indices of the subarray. This can be done by tracking the start index of the current maximum sum as you iterate.


Example: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ] -> The subarray is [4, -1, 2, 1] with indices 3 to 6.

Maximum Sum Subarray in a Circular Array: This is a classic extension. The maximum sum subarray can either be a standard contiguous subarray or a "wrapping" one that goes from the end of the array to the beginning.

Solution: Find the maximum sum of a non-wrapping subarray (using Kadane's). Then, find the minimum sum subarray (by applying Kadane's to the negated array). The maximum sum of a wrapping subarray is (Total sum of array) - (Minimum subarray sum). The final answer is the maximum of these two values.

Maximum Product Subarray: This is a variation that requires a slight modification. Since a negative number multiplied by another negative number can result in a positive, you need to keep track of both the maximum and minimum products ending at the current position.

