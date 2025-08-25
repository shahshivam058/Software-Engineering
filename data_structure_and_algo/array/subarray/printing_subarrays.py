"""
Using Nested Loops
This is the most fundamental and widely used method for printing all subarrays. It works by iterating through all possible start and end points of a subarray.
Outer Loop: This loop iterates from the first element to the last, selecting the starting point of the subarray. Let's call the index i.
Inner Loop: This loop iterates from the starting point (i) to the end of the array, selecting the ending point of the subarray. Let's call the index j.\
Innermost Loop: This loop iterates from the starting point (i) to the ending point (j) and prints the elements of the current subarray.


This method is simple to understand but can be inefficient for very large arrays. The time complexity of this approach is O(n ** 3)

function printSubarrays(array):
    n = length of array
    for i from 0 to n-1:
        for j from i to n-1:
            // The subarray is from index i to j
            for k from i to j:
                print array[k]
            print a newline

"""

def print_subarray_nested_loop(arr) :
    n = len(arr) 

    for start_index in range(n) :
        for ending_index in range(start_index,n): # we can create a  list here and rather than printing all  element one by one add to list and print in end 
            subarry = [] 
            for index in range(start_index , ending_index + 1) : # range excludes the last index so we have to do ending index + 1 to also get last veriable  
                # print(arr[index] , end = " ")
                subarry.append(arr[index])
            print(subarry)
    
arr =[1 , 2 , 3 , 4 ,5]
# print(print_subarray_nested_loop(arr))


"""
More Efficient Nested Loops

We can optimize the printing process by eliminating the innermost loop. Instead of a third loop, we can print the subarray as we build it with the inner loop.

Outer Loop: Selects the starting point (i).
Inner Loop: Selects the ending point (j) and simultaneously prints the elements from the starting point.

function printSubarraysOptimized(array):
    n = length of array
    for i from 0 to n-1:
        currentSubarray = empty list
        for j from i to n-1:
            append array[j] to currentSubarray
            print currentSubarray

Time Complexity = o(n ** 2)
"""

def print_subarray_optimized_solution(arr) :
    n = len(arr) 

    for start_index in range(n) :
        subarray = []
        for end_index in range(start_index , n) :
            subarray.append(arr[end_index])
            print(subarray)

# print(print_subarray_optimized_solution(arr))


"""
The sliding window technique is more commonly used to solve specific subarray problems (like finding the maximum sum), but a variation can be used to 
generate subarrays. Instead of nested loops for start and end points, you can use two pointers (start and end) and increment the end pointer to expand the 
window.

The Two-Pointer Approach
The sliding window for this purpose uses two pointers: a start pointer and an end pointer.
Outer Loop: The start pointer iterates from the beginning of the array to the end. This fixes the beginning of the subarray.
Inner Loop: The end pointer starts at the same position as the start pointer and moves forward. This action "expands" the window, effectively creating all possible subarrays that begin at the start position.
Print: Inside the inner loop, the elements from the start to the end pointer represent the current subarray. You can print these elements.



"""

def subarray_most_optimized(arr) :
    n = len(arr)

    for start_index in range(n) :
        for ending_index in range(start_index , n) :
            subarray = arr[start_index : ending_index + 1]
            print(subarray)

# subarray_most_optimized(arr)


"""
Printing Fixed-Size Subarrays
For a fixed size k, you only need one loop that goes from the start of the array up to the point where a window of size k can be formed.
Iterate to the end: Loop through the array from index 0 up to n - k, where n is the length of the array. This i index represents the starting point of your subarray.
Define the window: The subarray will be from index i to i + k - 1.
Print: Print the elements within this window.

function printFixedSizeSubarrays(array, k):
    n = length of array
    if k > n:
        print "Error: Subarray size is greater than array size."
        return

    for i from 0 to n - k:
        // The subarray starts at 'i' and has length 'k'
        for j from i to i + k - 1:
            print array[j]
        print a newline


"""


def fixed_size_subarrays(arr):
    n = len(arr) 
    k = 3

    # The outer loop correctly sets the starting index.
    # It must stop at n - k to prevent out-of-bounds errors.
    for start_index in range(n - k + 1):
        # The end index is simply the start index plus k - 1
        end_index = start_index + k - 1
        # This slice creates the fixed-size subarray
        print(arr[start_index : end_index + 1])

# Example usage
arr = [1, 2, 3, 4, 5]


fixed_size_subarrays(arr)




"""
Maximum subarray sum

This is the most straightforward but least efficient method. It involves generating every single subarray of length B, calculating the sum for each one, 
and keeping track of the maximum sum found so far.

Logic: Use a nested loop. The outer loop iterates from the first possible starting position (i = 0) to the last possible starting position (i = N - B). 
The inner loop calculates the sum of the subarray starting at i and ending at i + B - 1.


Below one is great code for printing fix sized sliding window 
the reason we just need start index and we need to know window size 
with help of start index we can genrate the 


outer we are looping till n - k + 1 : it represent last window of size k if we reached n index we dont have any element on right we cant access it 
inner loop we are looping for b times which helps us to print all element within a window 
with help of b we can get actual elemenmt 

A[start index + j]  
for j = 0 print first elemet 
for j = 1 represent 2nd element in window 
for j = 2 represenmt 3rd element in window 


and so on 


"""

class Solution:
    # @param A : list of integ ers
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        n = len(A) 
        result = 0

        for start in range(n - B + 1):
            total_sum = 0
            for j in range(B):
                total_sum = total_sum + A[start + j]
            
            result = max(result , total_sum)
                
        
        return result
         