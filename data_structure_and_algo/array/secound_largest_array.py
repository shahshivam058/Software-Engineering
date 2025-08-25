def secound_largest_array(arr) :
    largest  = 0 
    secound_largest = 0 

    for index in range(len(arr)):
        largest = max(largest , arr[index])

    
    for index in range(len(arr)):
        if arr[index] != largest :
            secound_largest = max(arr[index] , secound_largest)
    

    return secound_largest

arr = [1 , 2 , 3 ,4 ,5]
print(secound_largest_array(arr))


def second_largest_array(arr):
    if len(arr) < 2:
        return None  # or raise an exception as needed
    
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None


"""
When we find a new largest number:

First, we "demote" the current largest to be the second largest

Then we update the largest with the new number

When we find a number that's not largest but bigger than current second:

We update the second largest, ensuring it's not equal to the largest

array should of minimum size 2 
"""