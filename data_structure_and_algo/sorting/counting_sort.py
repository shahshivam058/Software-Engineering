"""
Counting Sort is a non-comparison-based sorting algorithm used for sorting elements when the range of input values is known and limited, 
typically for integers.

Instead of comparing elements (like quick sort or merge sort), it counts how many times each value appears, then reconstructs the sorted array based on those counts.

Elements are non-negative integers
The range of elements is not very large compared to the number of elements


"""

from collections import OrderedDict

def count_sort_sorted_order(arr):
    freq = {}
    result = []

    for num in arr :
        freq[num] = freq.get(num , 0) + 1
    
    ordered_dict = OrderedDict()
    for key in sorted(freq):
        # ordered_dict[key] = freq[key]
        result.extend([key] * freq[key])
    
    # for value , ooc in ordered_dict.items() :
    #     result.extend([value] * ooc)
    
    return result

arr = [4, 2, 2, 8, 3, 3, 1]
print(count_sort_sorted_order(arr))

"""

The input is made of non-negative integers

The range (k) of elements is not significantly larger than the number of elements (n)

Operates on the count array of size k → O(k)



we are visiting all element n to create a freq map 
we are creating an k sized dict containing freq and value 

o(n + k) both time and space complexity 
use same to genrate array 


"""


"""

Given array a of size n all element are in range between 1 to n sort arr

Sorting array : n**2 if we use bubble sort slection or quick sort
can we store freq of all elements from 1 to n  

range is already given so we can directly use that 


"""