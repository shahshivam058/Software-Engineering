"""
Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.

The goal is to compute an output array where each element output[i] is the product of every element in the input array except for the element at index i. This is exactly what your code and the provided explanations aim to do.


Approach 1: Using Two Auxiliary Arrays
This approach involves two passes over the array to compute the products of elements to the left and right of each index.
Left Products Array: Create an array, let's call it left_products, of the same size as the input array A. Iterate from left to right, and for each index i, store the product of all elements to its left.
left_products[0] will be 1 (as there are no elements to the left of the first element).
left_products[i] will be the product of A[0] to A[i-1].
Right Products Array: Create another array, right_products, of the same size. Iterate from right to left, and for each index i, store the product of all elements to its right.
right_products[n-1] will be 1 (as there are no elements to the right of the last element).
right_products[i] will be the product of A[i+1] to A[n-1].
Final Product Array: Create the final product_array. Iterate through the original array A from index i = 0 to n-1. The value for each element in the product_array will be the product of the corresponding elements from the two auxiliary arrays: product_array[i] = left_products[i] * right_products[i]. This effectively gives you the product of all elements excluding A[i].
This approach has a time complexity of O(n) because you make three linear passes over the array. The space complexity is also O(n) because you use two additional arrays.

Approach 2: Using a Single Pass with a Variable
This is a more optimized approach that uses a single pass and a temporary variable to reduce the space complexity.
Calculate Left Products: Create the final product_array and initialize all its elements to 1. Iterate through the array A from left to right. At each index i, store the product of elements to the left of A[i] in product_array[i].
Initialize a variable left_product to 1.
For i from 0 to n-1, set product_array[i] = left_product.
Then, update left_product by multiplying it with A[i]. This prepares left_product for the next iteration.
Calculate Right Products: Now, iterate through the array A from right to left.
Initialize a variable right_product to 1.
For i from n-1 to 0, update the product_array element by multiplying it with right_product: product_array[i] *= right_product.
Then, update right_product by multiplying it with A[i].



"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        left_product = [1] * n
        right_product = [1] * n
        product_array = [1] * n

        for index in range(1 , n):
            left_product[index] = left_product[index - 1] * A[index - 1]  # we are storing multiplication till last index
        
        for index in range(n - 2, -1 , -1):
            right_product[index] = right_product[index + 1] * A[index + 1] 
        
        for index in range(n) :
            product_array[index] = left_product[index] * right_product[index] # stores all product 
        
        return product_array



class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        product_array = [1] * n

        left_total = 1 
        right_total = 1

        for index in range(n):
            product_array[index] *= left_total
            left_total =  A[index]  * left_total
        

        for index in range(n - 1 , -1 , -1):
            product_array[index] *= right_total
            right_total =  A[index]  * right_total
        
        return product_array
        


 