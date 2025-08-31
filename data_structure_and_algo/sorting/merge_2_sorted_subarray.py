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

The idea is simple but subtle:

If you have two parts of an array that are individually sorted, then combining them into one big sorted array is much easier than sorting everything from scratch.
To do this safely, most textbook implementations copy each part into temporary subarrays before merging.

In-place merging: There are algorithms to merge without making extra arrays, but they’re trickier (often involving shifting elements around, which can push time complexity toward
"""

def merge_2_sorted_subarray(arr , s , m , e) :
    arr1 = arr[s : m + 1] # start to mid + 1  to get values till mid as slicing return result till mid - 1
    arr2 = arr[m + 1 : e + 1] # from mid to end 

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


    arr[s : e + 1] = result # adding as a part

    return arr


arr = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
s = 2
m = 6
e = 9
print(merge_2_sorted_subarray(arr , s , m , e))
