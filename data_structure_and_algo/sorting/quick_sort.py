"""
Quick Sort: Detailed Explanation
Quick Sort is a highly efficient divide-and-conquer sorting algorithm that works by 
partitioning an array around a chosen "pivot" element and recursively sorting the resulting subarrays. Here's a comprehensive breakdown:

Core Concept
Pivot Selection: Choose an element from the array (the "pivot").

Partitioning:

Rearrange the array so all elements smaller than the pivot are on its left.

All elements larger than the pivot are on its right.

Recursion: Apply the same process recursively to the left and right subarrays.


Partitioning Process (Lomuto Scheme)
This is the most common partitioning method. Steps for partitioning arr[low..high]:

Pivot Selection: Choose the last element as pivot (pivot = arr[high]).

Index Initialization:

i = low - 1 (tracks the position where the pivot will be inserted).

Traverse and Swap:

For each element arr[j] from low to high-1:

If arr[j] <= pivot, increment i and swap arr[i] and arr[j].

Place Pivot:

Swap arr[i + 1] with arr[high] (pivot moves to its final position).

Return Pivot Index: i + 1.

Visual Example (Partitioning [10, 80, 30, 90, 40, 50, 70] with pivot=70):



Quickselect (Finding the k-th Largest/Smallest Element): This is a direct and highly efficient application. Quickselect uses the partitioning logic of Quick Sort to find the k-th smallest (or largest) element in an array in average O(n) time. Instead of recursively sorting both partitions, it only recurses into the partition that contains the desired k-th element.
Dutch National Flag Problem (3-Way Partitioning): Given an array containing three distinct elements (e.g., 0s, 1s, and 2s), sort them such that all 0s come first, then all 1s, then all 2s. This is a classic partitioning problem that can be solved efficiently with a single pass, similar to Quick Sort's partitioning.
Partitioning Around a Value: Given an array and a specific value X, rearrange the array such that all elements less than X come before X, and all elements greater than X come after X. This is the fundamental step of Quick Sort.
Sorting a Partial Array/Subarray: Sort only a specific range of elements within a larger array. The Quick Sort function can be called with adjusted low and high indices.
Hybrid Sorting Algorithms (IntroSort): Explain how Quick Sort is part of hybrid sorting algorithms like IntroSort (used in C++'s std::sort). IntroSort starts with Quick Sort but switches to Heap Sort if the recursion depth gets too large (to avoid the O(n 
2
 ) worst case) and uses Insertion Sort for very small sub-arrays.
Finding the Median: Efficiently finding the median of an unsorted array can be done using the Quickselect algorithm.
Problems Requiring Efficient Partitioning: Any problem where you need to group elements based on a certain property (e.g., positive/negative numbers, even/odd numbers) can leverage the partitioning concept.






1. Time Complexity
Best Case: O(n log n)
Scenario: The pivot always divides the array into two equal or nearly equal parts.

Why?

Each partitioning splits the array into two halves → log n recursion levels.

Each level processes n elements (partitioning takes O(n) per level).

Example:

Pivot is always the median (e.g., using "median-of-three" pivot selection).

Average Case: O(n log n)
Scenario: Pivot is randomly selected (balanced splits on average).

Why?

Even if splits are not perfectly equal, expected recursion depth is still O(log n).

Each level still takes O(n) time for partitioning.

Example:

Using randomized Quick Sort (pivot chosen randomly).

Worst Case: O(n²)
Scenario: The pivot is always the smallest or largest element (highly unbalanced partitions).

Why?

Recursion depth becomes O(n) (like a linked list traversal).

Each partitioning step still takes O(n) time.

Examples:

Array is already sorted (if pivot is the first/last element).

All elements are identical (if not optimized).

2. Space Complexity
Best/Average Case: O(log n) (due to recursion stack depth).

Worst Case: O(n) (unbalanced recursion stack).

Why?
Quick Sort is in-place, meaning it doesn’t use extra memory for temporary arrays (unlike Merge Sort).

However, recursion stack space depends on partitioning:

Balanced splits: Stack depth = log n.

Unbalanced splits: Stack depth = n.







"""

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        pi = hoare_partition(arr, low, high)
        # Recursively sort left and right of pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choose the first element as pivot
    i = low - 1
    j = high + 1

    while True:
        # Move 'i' rightward until an element >= pivot is found
        i += 1 # The first move of i += 1 puts i on the first valid element (i.e., low).

        while arr[i] < pivot:
            i += 1

        # Move 'j' leftward until an element <= pivot is found
        j -= 1 # The first move of j -= 1 puts j on the last valid element (i.e., high).

        while arr[j] > pivot:
            j -= 1

        # If pointers cross, return partition index
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

arr = [8, 4, 7, 3, 10, 2]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
