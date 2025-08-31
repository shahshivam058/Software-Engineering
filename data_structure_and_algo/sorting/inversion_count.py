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

Given an array of size n Just count The number of i , j Index such that 
I < J and a[i] > a[j]

Identify No of inversion Pairs 

Count The number of pairs where larger one on left and smaller one on right side 
[ 3 , 1 , 2]


identify all the pair 

Why sorting approch will not work 
Index change hence we cant get correct place
More element we have more Unsorted they are


if we have 2 sorted array counting inversion becomes easy 


we will have 2 sorted array A and B 

WE will compare first element Both 


If both array are sorted 

we starting by comparing the first element 

check first element in both array 
so if a[i] < b[i] then all element including b[i] to n will be larger then a[i] so we can directly add a count 
so merging 2 sorted array will be correct 

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
            inversion += len(arr1) - i  # All remaining elements in arr1 are greater => inversions we have added here as it is part of conditipon arr1[i] > arr2[j]

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
