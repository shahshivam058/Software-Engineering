"""
We Have Given Matrix of size N * N 

Primary diagonal: runs from the top-left corner to the bottom-right corner.

Secondary diagonal: runs from the top-right corner to the bottom-left corner.

Sum = Primary Diagonal Sum + Secondary Diagonal Sum 

👉 One catch: if the matrix has odd dimensions (like 3×3, 5×5), the center element gets counted twice (once in each diagonal). Typically, we subtract it once to avoid double-counting.
Primary diagonal =  1 + 5 + 9 = 15
Secondary diagonal = 3+5+7 = 15

Total =  15 + 15 - 5 = 25

"""

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        res = 0 

        for i in range(n) :
            res = res + mat[i][i]
            res = res + mat[i][n - i - 1]
        
        return res -  (mat[n // 2][n // 2] if n & 1 else 0)
