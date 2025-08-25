The Sliding Window technique is an algorithmic approach used to solve problems on arrays or strings. It's particularly useful for finding a subarray, substring, or a "window" of a specified size that meets a certain condition. The core idea is to transform a brute-force approach with nested loops into a single-pass, linear-time solution, improving efficiency from O(n ** 2) to O(n).



The Core Concept 🪟 :

Imagine you have a window of a certain size (let's say k) that you can slide across a larger array. Instead of re-calculating the sum, average, or other property of the elements in the window every single time, you perform a simple update.

A key analogy is a physical window sliding along a track. As the window slides one step to the right, a new element enters from the right, and one old element exits from the left.

Add new element: Include the element at the right side of the window.

Remove old element: Exclude the element at the left side of the window.

This process ensures that at each step, you're only performing a constant number of operations, leading to an overall efficient algorithm.

The Fixed-Size Sliding Window is an algorithmic technique used to solve problems on arrays or strings by maintaining a "window" of a constant, predetermined size (k) as it moves across the data structure. Instead of re-calculating a property (like a sum, average, or count) for each new window, the algorithm efficiently updates it in constant time, leading to a linear time complexity of O(n).

The Core Concept 🪟
Imagine you have a physical window of a fixed width that slides along a continuous strip of data. At each step, a new element enters the window from the right, and an old element exits from the left. By simply adding the new element's value and subtracting the old one's, you can find the property of the new window without processing all k elements again.

This approach transforms a brute-force solution with a nested loop (which has an O(n⋅k) or O(n ** 2) complexity) into a single-pass, O(n) solution. The two pointers, often called start and end, define the boundaries of this window.

The Algorithm
The process can be broken down into two main phases: building the initial window and then sliding it.

Build the Initial Window:

Initialize two pointers, start = 0 and end = 0.

Use a loop to move the end pointer to the right until the window size reaches k.

During this initial phase, calculate the property of the first k elements (e.g., sum, product, etc.).

Slide the Window:

Start a loop that moves the window one step at a time. This is done by incrementing both the start and end pointers.

Update the Property: Before moving, subtract the element at array[start] from your current calculation and add the new element at array[end]. This is the core efficiency gain of the technique.

Store the Result: After each slide, store or compare the updated property with the best result found so far (e.g., the maximum sum, minimum average).

The Dynamic-Sized Sliding Window is an algorithmic technique used to solve problems on arrays or strings where the size of the "window" is not fixed and can change during the traversal. Instead of maintaining a constant-sized window, this approach expands and contracts the window based on a condition, making it highly flexible and efficient. It's particularly useful for finding the longest, shortest, or total count of subarrays or substrings that satisfy a specific property.

The Core Concept ⚖️
Unlike its fixed-size counterpart, a dynamic-sized window doesn't simply slide one step at a time. It uses two pointers, start and end, to define the window.

The end pointer moves to the right to expand the window, including a new element in the current calculation.

The start pointer moves to the right to contract the window, shrinking its size and removing an element from the left.

The decision to expand or contract is based on whether the elements currently in the window satisfy a given condition. For example, if the sum of elements exceeds a target, you must shrink the window to bring the sum back down.

The Algorithm
The process of a dynamic-sized sliding window involves a single loop that moves the end pointer, with a conditional inner loop or block that moves the start pointer.

Initialize Pointers and Variables:

Set both the start and end pointers to the beginning of the array (e.g., start = 0, end = 0).

Initialize variables to track the state of the current window (e.g., current_sum, character_frequency_map) and the best result found so far (e.g., max_length, min_length).

Expand the Window:

Use a for or while loop that iterates the end pointer from 0 to n-1, where n is the length of the data structure.

Inside the loop, add the element at array[end] to your current calculation. For example, if you're tracking a sum, you'd add array[end] to current_sum.

Contract the Window (Conditional Shrinking):

Immediately after expanding, check if the current window violates the given condition (e.g., current_sum > target, or the number of unique characters exceeds k).

If the condition is violated, use an inner while loop to move the start pointer to the right. As you move the start pointer, subtract the element at array[start] from your current calculation to reflect the change in the window. The inner loop continues until the condition is no longer violated.

Update the Result:

After each expansion and potential contraction, update your result variable. For example, if you're finding the longest subarray, you'd update max_length = max(max_length, end - start + 1).




Fixed-Size Window Problems
These problems involve a window of a constant size, where you need to calculate a property for every contiguous subarray of that specific length.

Maximum/Minimum Sum of a Subarray of Size k: Find the subarray of a given size k that has the highest or lowest sum. This is a classic example where the window slides one element at a time, and the sum is updated by adding the new element and subtracting the old one.

Average of All Subarrays of Size k: Calculate the average for all contiguous subarrays of a given size k.

First Negative Integer in Every Window of Size k: Find the first negative number in each subarray of a fixed size.

Maximum/Minimum of a Window: Find the maximum or minimum element in every subarray of size k.

Dynamic-Size Window Problems
In these problems, the window size is not fixed and changes based on a condition. The window expands until a condition is met and then contracts to re-satisfy that condition.

Longest Substring with No Repeating Characters: Find the longest substring that contains no duplicate characters. The window expands, and if a duplicate is found, it shrinks from the left to remove the duplicate.

Longest Substring with At Most K Distinct Characters: Find the longest substring that has no more than k unique characters. The window expands until the count of unique characters exceeds k, then it shrinks from the left.

Minimum Size Subarray Sum: Find the smallest contiguous subarray whose sum is greater than or equal to a given target value. The window expands to meet the sum requirement and then shrinks to find the minimum size.

Count of Subarrays with Product Less than K: Find the number of contiguous subarrays whose product is less than a given k. The window expands, and if the product exceeds k, it shrinks to re-satisfy the condition.

Permutation in a String: Check if a string contains a permutation of a pattern string. A dynamic window is used to find a substring of a certain length that has the same character frequency as the pattern.

Longest Substring with Same Letters After Replacement: Find the longest substring with the same letters after replacing up to k letters. The window expands, and if the number of replacements needed exceeds k, it contracts.

