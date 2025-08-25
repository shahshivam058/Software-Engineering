"""

Brute force approch :

Brute force approch that we can use here is just to use 3 nested loops 
1st Loop starting index in subarray 
2nd loop from i to n : represents the end of index 
3rd loop : loop though array and add to sum and added to result 

optimal approch : 

we can just improve over a above approch by building apprich and performing opretions 
2 loops 

another approch we can use is prefix sum we can genrate both start and end and just use prefix sum and return result 



we need to study more about contribution technique 
"""



def sum_of_subbarray(arr) :
    n = len(arr)
    result = []

    for start in range(n) :
        total_sum = 0 
        for end in range(start , n):
            total_sum += arr[end]
            result.append(total_sum)
    
    return result

arr = [1 , 2 ,3 ,4 ,5]
print(sum_of_subbarray(arr))


"""
Array Contribution Technique Explained

The Array Contribution Technique (also known as the "Contribution of Elements" method) is an optimization strategy used to solve array-based problems 
efficiently. Instead of processing all possible subarrays explicitly (which would be O(n²)), it calculates each element's individual contribution to the final 
result across all relevant subarrays. This reduces time complexity to O(n) or O(n log n) in many cases.


Key Insight: For each element in the array, determine how many times it contributes to the solution (e.g., how many subarrays include it under specific conditions like being the minimum/maximum).

Result = A[I] * contribution

Let's use a simple example: arr = [A, B, C]

Number A: This number is at the beginning. It's part of the subarrays [A], [A, B], and [A, B, C]. So it appears 3 times.
Number B: This number is in the middle. It's part of the subarrays [B], [A, B], [B, C], and [A, B, C]. It appears 4 times.
Number C: This number is at the end. It's part of the subarrays [C], [B, C], and [A, B, C]. It appears 3 times.

Contribution formula = (i + 1) * (n - i)

(i + 1)
This part of the formula counts the number of possible starting points for a subarray that includes arr[i]. A subarray that includes arr[i] can start at any index from 0 up to i.
For an element at index i, the possible starting indices are:
Index 0
Index 1
...
Index i
The total count of these starting points is (i - 0) + 1, which simplifies to i + 1.




(n - i)
This part of the formula counts the number of possible ending points for a subarray that includes arr[i]. 
A subarray that includes arr[i] can end at any index from i up to n - 1.
For an element at index i, the possible ending indices are:
Index i
Index i + 1
...
Index n - 1
The total count of these ending points is (n - 1) - i + 1, which simplifies to n - i.



"""