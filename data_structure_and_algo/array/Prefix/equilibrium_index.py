"""
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

Note:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.


Brute force approch :

Brute force approch we can use here is 
we can genrate both prefix sum and suffix sum 
prefix sum array where that array i stores sum of all element from 0 to i
suffix sum array  where index i store sum from i to n

we are looping over the all index in array and counting sum till i index and sum from i + 1 to n 
left_sum = prefix_array[index] - A[index] # it allows us to genrate the 
right_sum = suffix_array[index] - A[index] #it allows us to get sum from i to n 

if left_sum == right_sum then equlibiran index 


Optimal Approch :
Algorithm:

- Find total_sum of all elements. = The code first calculates the sum of all elements in the array. This is a crucial pre-computation step. It allows us to determine the right sum at any given index without having to iterate through the rest of the array each time.
- Initialize left_sum = 0. = A variable left_sum is initialized to 0. This variable will keep a running total of the sum of elements to the left of the current index as we iterate through the array.
- Loop over each index i:
- Right sum can be found as: right_sum = total_sum - left_sum - arr[i]   
- If left_sum == right_sum, i is an equilibrium index.
- Add arr[i] to left_sum.

The left_sum is the sum of all elements to the left of the current element.
The sum of elements to the right of the current element is calculated as total_sum - left_sum - num. This works because:
total_sum is the sum of all elements in the array.
left_sum is the sum of elements before the current one.
num is the value of the current element itself.
By subtracting left_sum and num from total_sum, we are left with the sum of all elements after the current one, which is the right sum.


"""

class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):

        n = len(A)
        prefix_array = [0] * n
        suffix_array = [0] * n 

        prefix_array[0]  = A[0]
        suffix_array[-1] = A[-1]

        for index in range(1 , n) :
            prefix_array[index] = prefix_array[index - 1] + A[index]
        
        for index in range(n - 2 , -1 , - 1 ):
            suffix_array[index] = suffix_array[index + 1] + A[index]

        
        result = -1
        for index in range(n) :
            left_sum = prefix_array[index] - A[index]
            right_sum = suffix_array[index] - A[index]
            if left_sum == right_sum  :
                return index
        
        return result
                



        

def equilibrium_indices(arr):
    total_sum = sum(arr)
    left_sum = 0
    result = []

    for i, num in enumerate(arr):
        if left_sum == (total_sum - left_sum - num):
            result.append(i)
        left_sum += num

    return result

# Example usage
arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_indices(arr))  # Output: [3, 6]
