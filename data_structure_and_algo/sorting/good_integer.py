"""
Given an array of integers, find if there exists a Noble Integer. 
A Noble Integer is an integer x such that the number of integers greater than x is exactly x.


To solve this, you:
Sort the array.
For each unique number, count how many elements are greater than it.
Check if that count equals the number itself.




"""

def nobleInteger(arr) :
    arr.sort()
    n = len(arr)

    for i in range(n) :
        if i < n - 1 and arr[i] == arr[i+1] : # we are checking  for the duplicate element sorted so next element will be same as next element then skip the element
            continue
        
        if arr[i] ==  (n - i - 1): # check if arr[i] element at ith index is x and remain element count is x 
            return 1 
        
        if arr[-1] == 0 : # we already sorted array so if the last element is 0 means all element before that are 0 and it doesnt satisfy the condition 
            return -1
    
print(nobleInteger([3, 2, 1, 3])) # Output: 1

