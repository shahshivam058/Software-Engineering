"""

You know:

The subarray arr[s..m] is sorted
The subarray arr[m+1..e] is also sorted
Your goal is to merge these two sorted subarrays into one sorted subarray, and place the result back into arr[s..e].


This creates two new arrays:

arr1 contains arr[s] to arr[m]
arr2 contains arr[m+1] to arr[e]

then apply 2 merge sorted array approch 

This replaces the original subarray arr[s..e] with the newly merged, sorted result.

You're using the classic merge step of merge sort:

Two sorted parts → merge them into one sorted part

Then, place the result back into the original array at the correct position


"""

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
s = 2
m = 6
e = 9
print(merge_2_sorted_subarray(arr , s , m , e))
