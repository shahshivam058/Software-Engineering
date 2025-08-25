
"""
You are given an array A of length N and Q queries given by the 2D array B of size Q×2.
Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].


Optimal Approch :

we can just use the prefix_sum kind approch 
where prefix sum arr[i] stores the total number of even numbers till arr[i]
we we found even even number just add else just copy last result 


"""
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def prefix_sum_even(self , A):
        n = len(A)
        result = [0] * n
        result[0] = 1 if (A[0] & 1 == 0) else 0 

        for index in range(1 , n) :
            result[index] = result[index - 1]  # we can just copy the value of last element as any way it will work even if number even or not
            if (A[index] & 1) == 0 :
                result[index] +=  1 # if number even then increase count
        return result
 


    def solve(self, A, B):
        n = len(A)
        even_count_array = self.prefix_sum_even(A)
        result = []


        for query in B:
            left = query[0]
            right = query[1]

            if left == 0 :
                result.append(even_count_array[right])
            else :
                result.append(even_count_array[right] - even_count_array[left - 1])
        
        return result



