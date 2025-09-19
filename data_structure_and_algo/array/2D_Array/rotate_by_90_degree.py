"""
You’re given an n x n matrix (square). Rotate it in place by 90° clockwise.
“In place” means you don’t return a new matrix—you rearrange the original one.

"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        matrix.reverse()

        for i in range(n):
            for j in range(i + 1 ,m):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                
        return matrix
