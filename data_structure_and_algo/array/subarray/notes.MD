A subarray is a contiguous part of an array. To put it simply, it's a sequence of one or more elements that are adjacent to each other within the original array. This is a fundamental concept in computer science, especially when dealing with data structures and algorithms.

Key Characteristics
Contiguity: This is the most important characteristic. The elements of a subarray must be consecutive in the original array. For example, in the array 
[1, 2, 3, 4], [2, 3] is a subarray, but [1, 3] is not, because the elements are not adjacent.

Size: A subarray can have any size from 1 (a single element) up to the size of the original array itself. A subarray that contains all the elements of the original array is considered a valid subarray.



Subarray vs. Subsequence vs. Subset
It's common to confuse a subarray with a subsequence or a subset. Here's a breakdown of the differences:

Subarray: Must be contiguous. [1, 2, 3, 4] ➡️ subarrays include [1, 2], [3, 4], [2, 3, 4].

Subsequence: Elements do not have to be contiguous but must maintain their relative order. [1, 2, 3, 4] ➡️ subsequences include [1, 3], [1, 4], [2, 4], and all subarrays are also subsequences.

Subset: Order and contiguity don't matter. It's simply a collection of elements from the original array. [1, 2, 3, 4] ➡️ subsets include {1, 3}, {2, 4}, {1, 2, 4}, and {4, 1, 3}.

Generating Subarrays
Let's consider an array arr with n elements. You can generate all possible subarrays by using nested loops. The outer loop can fix the starting point of the subarray, and the inner loop can extend the subarray to the right, creating all possible ending points.

For an array [1, 2, 3]:

Starting at index 0:

[1]

[1, 2]

[1, 2, 3]

Starting at index 1:

[2]

[2, 3]

Starting at index 2:

[3]

This gives us a total of 3+2+1=6 subarrays.

In general, for an array of size n, the total number of non-empty subarrays is given by the formula:


n(n+1) // N
​
 
For an array with 5 elements, there are  

5(6) // 2 =15 possible subarrays.

Importance and Applications
Subarrays are crucial in many algorithmic problems. For example:

Kadane's Algorithm: Used to find the maximum sum of a contiguous subarray.

Sliding Window Technique: A common approach for solving problems on arrays or lists, where a fixed-size or variable-size "window" (which is essentially a subarray) slides over the data.

Prefix Sum: Involves pre-calculating sums of subarrays to answer queries efficiently.

Understanding subarrays is a prerequisite for tackling these and many other advanced programming challenges.







Subarray: A subarray is a contiguous part of an array. The elements must be consecutive in the original array, and their relative order is maintained.
Contiguity: Yes
Order: Yes
Example: For [1, 2, 3, 4], [2, 3] is a subarray. [1, 3] is not.
The number of non-empty subarrays for an array of size n is 
fracn(n+1)2.

Subsequence: A subsequence is a new sequence formed from the original by deleting zero or more elements without changing the order of the remaining elements. The elements do not have to be contiguous.
Contiguity: No
Order: Yes
Example: For [1, 2, 3, 4], [1, 3, 4] is a subsequence. You get it by removing the '2'.
The number of subsequences for an array of size n is 2 ** n
 . This includes the empty subsequence.

Subset: A subset is a collection of elements from the original array where neither contiguity nor order matters. It's a fundamental concept from set theory. A subset is simply a group of elements from the original set.


Contiguity: No

Order: No

Example: For [1, 2, 3, 4], {1, 4} and {4, 1} are the same subset.

The number of subsets for a set of size n is also 2 ** n

 . This includes the empty set.


---

## **1. Core Definitions & Basics**

* **Subarray vs. Subsequence vs. Subset** — differences in continuity and order.
* **Fixed-size vs. Variable-size subarrays**.
* **Prefix sums** — to quickly calculate sum/range queries.
* **Sliding window basics** — shrinking and expanding a window.

---

## **2. Brute Force & Complexity**

* Generating all subarrays (`O(n²)` start/end loops).
* Computing sums, mins, or maxes in all subarrays.
* Time complexity trade-offs — when brute force is okay vs. when you need optimization.

---

## **3. Sliding Window Patterns**

* **Fixed-length sliding window**
  e.g., max sum of subarray of length `k`.
* **Variable-length sliding window**
  e.g., smallest subarray with sum ≥ target.
* **Window with condition**

  * At most `k` distinct elements.
  * At most `k` replacements to make all elements the same.

---

## **4. Prefix Sum & Hash Map Tricks**

* **Prefix sum for sum range queries**.
* **Subarray sum equals `k`** (`O(n)` with hash map storing prefix sums).
* **Handling negative numbers** — why sliding window might fail.
* **2D prefix sums** for submatrix problems.

---

## **5. Kadane’s Algorithm & Variants**

* **Maximum subarray sum** — `O(n)`.
* **With constraints**:

  * Maximum sum of size ≤ `k`.
  * Circular array version.
  * With deletion allowed (max sum with one element removed).

---

## **6. Monotonic Data Structures**

* **Monotonic queue** for max/min in a sliding window.
* **Next greater/smaller element** concepts for range problems.

---

## **7. Binary Search on Answer**

* **Minimum subarray length** with constraints.
* **Maximum average subarray** — binary search with prefix sums.

---

## **8. Two Pointers**

* For sorted arrays — sum-based conditions.
* Shrinking/growing range to satisfy property.

---

## **9. Advanced Patterns**

* **Subarrays with product less than `k`**.
* **Count subarrays with bounded maximum**.
* **Number of subarrays divisible by `k`** (modulo + prefix sum trick).
* **Bitwise subarray problems** — AND, OR, XOR constraints.
* **Median of subarray** (binary search + prefix sums).
* **Transforming problem to subarray counting** (often hidden in disguise).

---

## **10. Special Cases for FAANG**

* **Subarray problems with streaming data** — think online algorithms.
* **Multi-dimensional subarray** (submatrix problems).
* **Sparse arrays or huge input constraints** — optimizing space/time.
* **Dynamic programming + subarrays** (e.g., partitioning arrays).
* **Greedy + subarray** — rare but appears in interval merging disguised as subarray.

---

## **11. Practice Problem Tags (LeetCode / FAANG)**

* **Easy:**

  * Maximum sum of fixed-size subarray
  * Find all subarrays summing to `k`
* **Medium:**

  * Minimum size subarray sum
  * Subarray product less than `k`
  * Longest substring with at most `k` distinct characters (string variant)
* **Hard:**

  * Shortest subarray with sum ≥ K (with negatives)
  * Maximum sum circular subarray
  * Count subarrays with median ≥ m
  * Sum of subarray minimums/maximums

---

If you want, I can turn this into a **study roadmap** with problem links and difficulty ordering so you can go from fundamentals to FAANG-level mastery without missing any trick. This would save you from jumping randomly between problems.

