"""
Given a 2D integer array matrix, return the transpose of the matrix.

The transpose of a matrix is formed by flipping it over its main diagonal.

That means the element at position (i, j) moves to (j, i).


Original matrix was 2 x 3 (2 rows, 3 columns).

Transposed matrix becomes 3 x 2.

So the transpose swaps rows and columns.

"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix) 
        COLS = len(matrix[0])
        
        res = [ [0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS) :
                res[c][r] = matrix[r][c]
        
        return res
