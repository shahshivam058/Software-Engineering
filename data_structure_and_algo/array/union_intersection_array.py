"""
Union of array :

In mathematics and programming, the union of two (or more) sets is the collection of all distinct elements that appear in any of the sets.
“Distinct” means no duplicates in the final result.
“Appear in any” means if an element is in either array, it should be in the union.
When we talk about the “union” of arrays, we generally mean:
“Combine all elements from the arrays into one list, remove duplicates, and optionally arrange them in some order.”

Brute Force approch :
- we can convert the both of array into set 
- we can directly apply set opretion that is union 

Using sets: O(n + m)

Brute force approch :

- we can create a new array named result 
- we can loop over both the array and add it to result if its not available 
- if element already available in result skip it

TC : O(n * m)

3RD Approch :
Most optimal approch we can use for union is we can use some thing similer to 2 merge sorted approch 
If arr1[i] < arr2[j] and check if arr1[i] not same as last element in result, add arr1[i] to the result and move i forward.
If arr1[i] > arr2[j] and check if arr2[j] not same as last element in result, add arr2[j] to the result and move j forward.
If they’re equal, add one of them to the result (to avoid duplicates) and move both pointers forward.


smallert element need to array and once excedded 

o(n + m ) 


intersection  of 2 arrays : The intersection of two arrays is the set of elements that appear in both arrays.
Order doesn’t matter (unless a problem specifies otherwise).

Brute Force Approch :
- brute force approch can be using using set opretions 


Brute force approch :
- 
Algorithm:
Initialize an empty list intersection_list.
For each element x in arr1:
For each element y in arr2:
If x equals y, add x to intersection_list and break the inner loop to avoid adding duplicates if x appears multiple times in arr2.
Time Complexity: O(n∗m), where n and m are the lengths of the two arrays. This is because for each of the n elements in the first array, we perform a linear scan of the second array, which has m elements.
Space Complexity: O(min(n,m)) in the worst case to store the intersection elements.





Optimal Approch :
optimal approch for intersection is very similer to union approch 
but we are 

Sort arr1 and arr2 if they are not already sorted. This step is crucial and affects the overall complexity.
Initialize two pointers, i = 0 for arr1 and j = 0 for arr2.
Initialize an empty list intersection_list.
While i < n and j < m:
If arr1[i] < arr2[j], increment i.
If arr1[i] > arr2[j], increment j.
If arr1[i] == arr2[j], we've found an intersection. Add arr1[i] to intersection_list and then increment both i and j. This is a key step to move past the current matching element.


When the pointer for the shorter array reaches its end, the loop condition (i < len(arr1) and j < len(arr2)) will immediately become false. At that point, the loop terminates. This is the correct behavior because once one array has been fully traversed, there can be no more common elements (intersections) with the remaining elements of the longer array.


"""


def union_arrays(arr1, arr2) :
    result = list()
    n = len(arr1)
    m = len(arr2)

    i = j = 0

    while i < n and j < m :
        if arr1[i] < arr2[j] :
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i] :
            if not result or result[-1] != arr2[j] : 
                result.append(arr2[j])
            j = j + 1
        else : # means both arr[i] and arr[j] are same 
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i = i + 1
            j = j + 1
    

    while i < n :
        if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
        i += 1
    
    while j < m :
        if not result or result[-1] != arr2[j] : 
                result.append(arr2[j])
        j = j + 1

    
    return result



def intersection_of_two_array(arr1, arr2) :
    n = len(arr1)
    m = len(arr2)

    result = []

    i = j = 0

    while i < n and j < m :
         if arr1[i] <  arr2[j] :
               i = i + 1
         elif arr2[j] < arr1[i] :
               j = j + 1
         else :
            if not result or result[-1] != arr1[i] :
                result.append(arr1[i])
                i = i + 1
                j = j + 1     
        

    return result

arr1 = [1 , 2 ,3 ,4 , 5]
arr2 = [3 , 4 ]

print(union_arrays(arr1 , arr2))
print(intersection_of_two_array(arr1 , arr2))