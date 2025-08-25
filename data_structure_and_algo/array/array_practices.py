import math

# def largest_element_in_array(arr) :
#     if len(arr)  == 0 or len(arr)  == 1:
#         return arr
#     largest = -math.inf
#     n = len(arr)

#     for index in range(n) :
#         if arr[index] > largest :
#             largest = arr[index]
    
#     return largest

# def smallest_element_in_array(arr) :
#     if len(arr)  == 0 or len(arr)  == 1:
#         return arr

#     smallest = math.inf
#     n = len(arr)

#     for index in range(n) :
#         if arr[index] < smallest :
#             smallest = arr[index]
    
#     return smallest

def largest_and_smallest_in_given_array(arr) :
    n = len(arr)
    if n == 0:
        return None, None
    if n == 1:
        return arr[0], arr[0]

    # Initialize smallest and largest with the first two elements
    if arr[0] > arr[1]:
        largest, smallest = arr[0], arr[1]
    else:
        largest, smallest = arr[1], arr[0]


    smallest = math.inf
    largest = -math.inf

    n = len(arr)

    for index in range(n) :
        if arr[index] > largest : largest = arr[index]
        if arr[index] < smallest : smallest = arr[index]
    
    return smallest , largest

def secound_largest_in_array(arr) :
    n = len(arr)
    if n < 2 :
        return None , None
    largest = secound_largest = -math.inf

    """
    we are looping over all elements in array 
    we have to identify both largest and secound largest 
    we Looping over all elements in array the main aim is to check largest and secound largest 
    so we will check if current element is greter then largest then we will promote the largest element to secound largest and new element will be largest 
    also we are checking if current element is not largest and its greter than secound largest then we are promoting that one to secound largest 
    """


    for index in range(n):
        if arr[index] > largest :
            secound_largest = largest
            largest = arr[index]
        
        elif arr[index] != largest and arr[index] > secound_largest: # or we can also write arr[index] < largest and arr[index] > secound_largest
            secound_largest = arr[index]
        

    return largest , secound_largest

def secound_smallest_in_array(arr) :
    n = len(arr)
    if n < 2 :
        return None , None
    smallest = secound_smallest = math.inf

    """
    we are looping over all elements in array 
    we have to identify both largest and secound largest 
    we Looping over all elements in array the main aim is to check largest and secound largest 
    so we will check if current element is greter then largest then we will promote the largest element to secound largest and new element will be largest 
    also we are checking if current element is not largest and its greter than secound largest then we are promoting that one to secound largest 
    """


    for index in range(n):
        if arr[index] < smallest :
            secound_smallest = smallest
            smallest = arr[index]
        
        elif arr[index] != smallest and arr[index] < secound_smallest: # or we can also write arr[index] < largest and arr[index] > secound_largest
            secound_smallest = arr[index]
        

    return smallest , secound_smallest

def third_largest_in_array(arr) :
    n = len(arr)
    if n < 3 :
        return None , None , None
    
    first = secound = third = -math.inf

    for index in range(n) :
        if arr[index] > first : # we are same promotion algo here if the number greter then first then use promotion algo 
            third = secound
            secound = first
            first = arr[index]
        elif first > arr[index] > secound : # we are checking if  element is smaller than first but greter than 2nd one than 2nd 
            secound = arr[index]
        elif secound > arr[index] > third: # we are checking if element is greter then 3rd but smallest then 2nd then assign to third 
            third = arr[index]
    
    return first , secound , third


def count_even_odd(arr) :
    total_even = 0
    total_odd = 0
    n = len(arr)

    for index in range(n) :
        if (arr[index] & 1) == 1:
            total_odd += 1
        else:
            total_even += 1
    
    return total_even , total_odd

arr = [1,2,3,4,5]

def count_positive_negative_zero(arr) :
    zero = positive = negative = 0 
    n = len(arr) 

    for index in range(n) :

        if arr[index] > 0 :
            positive += 1
        elif arr[index]  == 0 :
            zero += 1
        else:
            negative += 1
    
    return zero , positive , negative

def count_oocurance_of_each_element(arr) :
    hash_map = {}

    for num in arr :
        hash_map[num] = hash_map.get(num , 0) + 1
    
    return hash_map

from typing import List, Tuple

def first_last_occurrence_unsorted(arr: List[int], target: int) -> Tuple[int, int]:
    first = last = -1
    for i, val in enumerate(arr):
        if val == target: 
            if first == -1: # we are if first oocurance then just check -1 value means default one 
                first = i
            last = i # everytime we found same value assign that to last 
    return first, last


# print(largest_element_in_array(arr))
# print(smallest_element_in_array(arr))
print(largest_and_smallest_in_given_array(arr))
print(secound_largest_in_array(arr))
print(secound_smallest_in_array(arr))
print(third_largest_in_array(arr))
print(count_even_odd(arr))
print(count_positive_negative_zero(arr))
print(count_oocurance_of_each_element(arr))