matrix = [[1 , 2, 3] , [4 , 5 , 6] , [7 , 8 , 9], [10 , 11 , 12]]

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        print(matrix[i][j] , end = " ")
    print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i] , end = " ")
    print()



for i in range(n):
    for j in range(i + 1 , m):
        matrix[i][j] , matrix[j][i] =  matrix[j][i] , matrix[i][j] 
    print()


print(matrix)


"""
When performing an in-place transpose on a square matrix (n
timesn), you only need to iterate through the upper or lower triangle and swap elements across the main diagonal. The main diagonal consists of elements where the row and column indices are the same (i.e., A[i][i]).

The algorithm for a square matrix is as follows:

Iterate through the matrix using nested loops. The outer loop i goes from 0 to n−1, and the inner loop j goes from i+1 to n−1. This ensures you are only processing each pair of off-diagonal elements once and avoiding the diagonal.

Inside the inner loop, swap the element at matrix[i][j] with the element at matrix[j][i].


"""