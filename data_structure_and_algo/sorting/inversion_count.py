"""
Inversion count measures how "unsorted" an array is. Specifically, it counts the number of inversions—pairs of indices (i, j) where:

i < j (left element comes before the right element)

arr[i] > arr[j] (left element is greater than the right element).


Why is Inversion Count Important?
Measure of Sortedness: Indicates how close an array is to being sorted.

0 inversions: Array is fully sorted.

Maximum inversions: Array is reverse-sorted.

Applications:

Analyzing sorting algorithms (e.g., Insertion Sort's runtime is proportional to inversion count).

Collaborative filtering and recommendation systems (comparing user preferences).

Computational biology (measuring sequence similarity).

it means all element on left are greter than right 




"""


def merge_sort(arr, s, e):
    if s >= e:
        return 0

    m = (s + e) // 2
    count = 0

    count += merge_sort(arr, s, m)
    count += merge_sort(arr, m + 1, e)
    count += merge_2_sorted_subarray(arr, s, m, e)

    return count


def merge_2_sorted_subarray(arr, s, m, e):
    arr1 = arr[s: m + 1]
    arr2 = arr[m + 1: e + 1]

    i = j = 0
    inversion = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
            inversion += len(arr1) - i  # All remaining elements in arr1 are greater => inversions

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    # Copy merged sorted subarray back into original array
    arr[s: e + 1] = result

    return inversion


# Test
arr = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
inversion_count = merge_sort(arr, 0, len(arr) - 1)
print("Inversion Count:", inversion_count)
print("Sorted Array:", arr)
