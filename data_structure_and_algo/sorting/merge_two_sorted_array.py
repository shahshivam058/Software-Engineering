
"""
2 merge sorted array is base of merge soft algo 

Given two sorted arrays with N and M elements. Merge them into one sorted array and Print them.

Output Format:
Print the merged sorted array in a line separated by space

output should contain result of both array in sorted order 

idea1  :

create a new array of size m + n 
add all elements of both the array 
sort the array 


idea2 :

we use the kind of pointer keep track of elements 
define 2 pointers  i and j with 0 
check the first pointer of both of array which ever is minimum add to result array and increase the pointer 
do the same untill all elements of one array are visited 

Now we might have visted one array but there might be some element in another we have to identify which array still have element which are not added to result 
Keep Track using Pointer 

check if pointer is at the end of array  or not 
if pointer is not at the end of array add all remaining element from array 

"""
def merge_two_sorted_array(arr1 , arr2) :
    """
     Merge 2 sorted array into one 
    """
    n = len(arr1)
    m = len(arr2)

    i = j = 0
    
    result = []
    while i < n and j < m :
        if arr1[i] < arr2[j] :
            result.append(arr1[i])
            i += 1 
        else :
            result.append(arr2[j])
            j += 1
    
    while i < n :
        result.append(arr1[i])
        i += 1 
    
    while j < m  :
        result.append(arr2[j])
        j += 1


    return result


arr1 = [7, 10, 11, 14]
arr2 = [3, 8, 9]

print(merge_two_sorted_array(arr1 , arr2))