"""
You are given an array A of length N and Q queries given by the 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].
For every query, the task is to calculate the sum of all even indices in the range A[B[i][0]…B[i][1]].

Note : Use 0-based indexing

"""


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        # Create a prefix sum array to store sums of elements at even indices
        prefix_sum_even_indices = [0] * n

        # Initialize the first element (index 0 is even)
        prefix_sum_even_indices[0] = A[0]
        
        # Build the prefix sum array
        for i in range(1, n):
            # Carry over the previous sum
            prefix_sum_even_indices[i] = prefix_sum_even_indices[i - 1]
            # If the current index is even, add the element to the sum
            if i % 2 == 0:
                prefix_sum_even_indices[i] += A[i]

        result = []

        # Process each query
        for query in B:
            left = query[0]
            right = query[1]

            if left == 0:
                # If the range starts at index 0, the sum is just the value at right
                result.append(prefix_sum_even_indices[right])
            else:
                # For any other range, subtract the prefix sum up to (left - 1)
                result.append(prefix_sum_even_indices[right] - prefix_sum_even_indices[left - 1])
        
        return result
    

# sum of all odd indexes
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        # Create a prefix sum array to store sums of elements at even indices
        prefix_sum_even_indices = [0] * n

        # Initialize the first element (index 0 is even)
        prefix_sum_even_indices[0] = 0
        
        # Build the prefix sum array
        for i in range(1, n):
            # Carry over the previous sum
            prefix_sum_even_indices[i] = prefix_sum_even_indices[i - 1]
            # If the current index is even, add the element to the sum
            if i % 2 != 0:
                prefix_sum_even_indices[i] += A[i]

        result = []

        # Process each query
        for query in B:
            left = query[0]
            right = query[1]

            if left == 0:
                # If the range starts at index 0, the sum is just the value at right
                result.append(prefix_sum_even_indices[right])
            else:
                # For any other range, subtract the prefix sum up to (left - 1)
                result.append(prefix_sum_even_indices[right] - prefix_sum_even_indices[left - 1])
        
        return result