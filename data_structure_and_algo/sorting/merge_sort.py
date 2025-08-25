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


def merge_sort(arr, s, e):
    # Base case: if subarray has 1 or 0 elements, it's already sorted
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
