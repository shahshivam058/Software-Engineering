"""
Optimal Approch :

where space is 0(1)
we can use matrix it self for identify row and col 
Rather than using extra list we can use the matrix it self 
use first row to represent row and first col to col 
"""

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        for i in range(n):
            if matrix[i][0] == 0:
                first_col_has_zero = True
        for j in range(m):
            if matrix[0][j] == 0:
                first_row_has_zero = True
        
        # use first row/col as markers
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # zero out based on markers
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # handle first row/col
        if first_row_has_zero:
            for j in range(m):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(n):
                matrix[i][0] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows , cols = set() , set()

        n = len(matrix)
        m = len(matrix[0])
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        
        for row in range(n):
            for col in range(m):
                if row in rows  or col in cols :
                    matrix[row][col] = 0

