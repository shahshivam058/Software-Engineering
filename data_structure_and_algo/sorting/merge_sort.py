"""

Merge Sort is a classic Divide and Conquer algorithm.

It works in three steps:

Divide: Split the array into two halves.
Conquer: Recursively sort each half.
Combine: Merge the two sorted halves into a single sorted array.


Counting Inversions: This is a classic application. An inversion in an array is a pair of indices (i,j) such that i<j but A[i]>A[j]. Merge sort can count inversions in O(nlogn) time by adding a counter to the merge step: whenever an element from the right subarray is moved to the merged array before an element from the left subarray, it indicates an inversion.
External Sorting: Explain how merge sort is used for external sorting (sorting data that is too large to fit into main memory). The data is divided into smaller chunks that fit in memory, sorted using an internal sort, and then these sorted chunks are repeatedly merged.
Merging K Sorted Lists/Arrays: Given k sorted lists (or arrays), merge them into a single sorted list. While a min-heap is often the most efficient solution (O(Nlogk) where N is total elements), a merge sort-like approach (recursively merging pairs of lists) can also solve this problem in O(Nlogk) time.
Finding Closest Pair of Points: In computational geometry, the divide and conquer approach of finding the closest pair of points can involve a merge-like step where points in a "strip" around the dividing line are merged and checked for closer pairs.
Divide and Conquer General Problems: Any problem that can be broken down into smaller, independent subproblems whose solutions can be efficiently combined can conceptually leverage the merge sort paradigm. Examples include:
Finding Majority Element: While other methods exist, a divide-and-conquer approach can be used.
Calculating the Median of Two Sorted Arrays: This can be done efficiently using a divide and conquer strategy similar to merge sort's partitioning.
Hybrid Sorting Algorithms: Explain how merge sort is part of hybrid sorting algorithms (like Tim Sort in Python and Java, or IntroSort in C++). These algorithms combine the best features of different sorts; for instance, Tim Sort uses merge sort for larger runs and insertion sort for smaller runs.




✅ Time Complexity Breakdown
Case	Time	Reason
Best	O(n log n)	Always divides + merges
Average	O(n log n)	No data-dependent behavior
Worst	O(n log n)	Even for reverse-sorted input



The recursion tree has depth log₂(n) (because each split halves the array)

At each level, merging takes O(n) time

So total = log n levels × O(n) work per level = O(n log n)



| Component             | Space                          |
| --------------------- | ------------------------------ |
| Merge arrays (output) | **O(n)**                       |
| Recursion stack       | **O(log n)**                   |
| **Total**             | $\boxed{O(n)}$ (dominant term) |




"""

"""

This is the function definition. It takes a list of numbers, nums, as its input. The self parameter suggests this method is part of a class.
This is the base case of the recursion. The division process stops when a subarray has a length of 0 or 1. A single-element list is inherently sorted, so it's returned as is. This is the conquer step for the smallest possible subproblem.
This line calculates the middle index of the current nums list. Using // ensures an integer division, which is crucial for indexing.
This is the recursive call for the left half. nums[:mid] creates a new list containing elements from the beginning up to (but not including) the middle index. The function then calls itself on this new list, which will continue the division process. This is the divide step.
This is the recursive call for the right half. nums[mid:] creates a new list containing elements from the middle index to the end. The function recursively sorts this part as well. This is also part of the divide step.
After the left and right halves have been sorted by the recursive calls (which eventually hit the base case and bubble back up), this line calls the merge function. The merge function takes the two sorted lists, left and right, and combines them into a single, sorted list, which is then returned. This is the combine step.





    def mergeSortWithHelper(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSortWithHelper(nums[:mid])
        right = self.mergeSortWithHelper(nums[mid:])
        
        return self.merge(left, right)

"""


def merge_sort(arr, s, e):
    # Base case: if subarray has 1 or 0 elements, it's already sorted

    """
    Parameters:

        arr: The array to be sorted
        s: Starting index of the current subarray
        e: Ending index of the current subarray

        Base Case: When s >= e, the subarray has 0 or 1 elements, which are inherently sorted
        Recursive Division:
        Calculate midpoint m to split the array into two halves
        Recursively call merge_sort on both halves
        This creates a binary tree of recursive calls until we reach single-element arrays
        Merging: After both halves are sorted, merge them using merge_2_sorted_subarray

        1. The "Two Sorted Arrays" Insight
            It's much easier to merge two already-sorted arrays into one sorted array than to sort an entire unsorted array from scratch
            The merging process can be done efficiently in linear time (O(n))

        2. The Recursive Insight
            Any array can be recursively divided into smaller subarrays until we reach the simplest case (arrays of size 0 or 1)
            Arrays of size 0 or 1 are inherently sorted by definition
            By working backwards from these simplest cases, we can build up sorted arrays from smaller sorted arrays

        3. The "Work Backwards" Principle
            Instead of trying to sort a large array directly, merge sort:
            Breaks it down into the simplest possible cases (single elements)
            Builds up the solution by merging these simple cases into larger sorted arrays




    """
    if s >= e:
        return

    # Find the midpoint
    m = (s + e) // 2

    # Recursively sort the two halves
    merge_sort(arr, s, m)
    merge_sort(arr, m + 1, e)

    # Merge the sorted halves
    merge_2_sorted_subarray(arr, s, m, e)



def merge_2_sorted_subarray(arr , s , m , e) :
    arr1 = arr[s : m + 1]
    arr2 = arr[m + 1 : e + 1]

    i = j = 0 

    result = []

    while i < len(arr1) and j < len(arr2) :
        if arr1[i] < arr2[j] :
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1) :
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2) :
        result.append(arr2[j])
        j += 1


    arr[s : e + 1] = result

    return arr


arr = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]

merge_sort(arr, 0, len(arr) - 1)
print(arr)

