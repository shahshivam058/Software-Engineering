- Chess 
- Sudoku 
- Snake and Ladder 
- excel sheet 

- All of above includes a grid which consist of rows and colums
- each square in box or intersection of row and col also called pixel 
- Laptop screen is consist of small small grid 
- Many of real world example uses rows and columns 
- 1D Array cant represent this kind of data 
- To deal with above kind of data and to store them we need 2d array 


- ARR[][] = new arr[r][c]
- we need to identify the size of array 
- r : represents row 
- c : represents colums
- Matrix will of  size R * C


- No of row = N - 1 
- No of colums = M - 1
- N * M : 
- N always represents rows count 
- M always represents colums count 
- Index of first Block - 0 , 0 
- Index of last Block - N - 1 , M - 1 

- Program should Print sum of all the rows :
n = len(matrix)
m = len(matrix[0]

for i in range(n): # we are the fix the index of rows 
    sum = 0 # we dont want to carry forward sum to next row so once each row done its 0 
    for j in range(m):
        sum += matrix[i][j]
    print(sum)

- Program should Print sum of all the colums :

n = len(matrix)
m = len(matrix[0])

for i in range(m):
    sum = 0
    for j in range(n):
        sum += matrix[j][i]
    print(sum)


TC = o(N*M)
SC = O(1)


Q Given a matrix of size m * n Print TOP LEF DIAGONAL TO BOTTOM RIGHT DIAGONAL:



n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        if i == j:
            print(matrix[i][j]))
            break


for i in range(n):
    print(matrix[i][i])


Q Given a matrix of size m * n Print BOTTOM LEFT DIAGONAL TO TOP RIGHT DIAGONAL:

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    print(matrix[i][n - i - 1])

Every Time Column Is increasing The main problem is Colum :
Top Right Column 
first row : 0 , n - 1
2nd row : 1 , n - 1 - 1
3rd row : 2  , n - 2 - 1
4th row : 3 , n - 3 - 1
5th row : 4 , n - 4 - 1
6th row : 5 , n - 5 - 1

from above pattern we know we can itrate through row and print the 
if we observ the pattern we can see every time row is increasing and column is decreasing 
so we can just write a 
Loop Through a each row 
it gives us row number from row number we can identify column number :
n - row - 1 


Q Given a square matrix Print all element about diagonal  above TL - BR  Diagonal 

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(i + 1):  
        print(matrix[i][j])


we can also print for top right to bottom left 

for i in range(n):
    for j in range(i + 1):  
        print(matrix[j][i])

Q Given a square matrix of size n * n Transpose Matrix :

def transpose_matrix(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with swapped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Iterate through the original matrix and populate the transposed one
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]


Q Rotate The Matrix By 90 Degree :

N = len(matrix)
M = len(matrix[0])

for i in range(N):
    for j in range(M):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        matrix[i].reverse()



Q Given The matrix of N * N Print The Boundry 

- we have to print boundry clock wise 
- for arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
- for above matrix the output will be 1 , 2  , 3  , 6 , 9 , 8 , 7 , 4 
- There are many ways to solve the problem 
- we have to print Boundry 
- we start from (0 , 0)
- our matrix is 5 * 5 and we want to print boundry then first print 4 number of 0th row 
- 4 numbers of last column 
- 4 numbers from last row in reverse
- 4 number from oth column reverse 
- how we got the 4 - for 5 * 5 matrix WE HAVE TO 4 
- for n * n matrix - we have to do print till n - 1
- Printing Boundry is nothing but using 
- n -1 first row - row number is constant col number is changing 
- n -1 last col - col number is constant row number is changing 
- n -1 last row in reverse - row number is constant col number is changing 
- n -1 first col in reverse - col number is constant row number is changing 
- end of one can be starting of another 

N = M = len(matrix)

i = j = 0 

for k in range(0 , n - 1):
    print(matrix[i][j])
    j = j + 1

for k in range(0 , n - 1):
    print(matrix[i][j])
    i = i + 1

for k in range(0 , n - 1):
    print(matrix[i][j])
    j = j - 1

for k in range(0 , n - 1):
    print(matrix[i][j])
    i = i - 1








Q Spiral Printing of square matrix 

- Print The outer most Boundry 
- The spiral print is nothing but Printing Boundry again and again 
- Outer one then inner one and repetedly 
- this time we cant do n - 1
- outer boundry it will work what about inner boundry 
- no of steps we used to take now is not constant 
- how will you print next boundry inner one 
- once done increase i 
- we are going to take steps 
- intial matrix of size = 6 * 6 
- first boundry - 0 , 0  n - 1
- next boundry - 1 , 1 n - 2
- next boundry - 2 , 2 n - 3

- i and j changeing + 1 + 1
- steps are getting decreased by 2 
- do it till steps are >= 1
- at the end of printing boundry it will reach 0 , 0 
-


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = m = len(matrix)
        i = j = 0 
        result = list()
        steps = n 
        
        while steps > 1:

            for k in range(steps-1):
                digit = matrix[i][j]
                result.append(digit)
                j = j + 1
            
            for k in range( steps-1):
                digit = matrix[i][j]
                result.append(digit)
                i = i + 1
            
            for k in range( steps -1):
                digit = matrix[i][j]
                result.append(digit)
                j = j - 1
            
            for k in range(steps-1):
                digit = matrix[i][j]
                result.append(digit)
                i = i - 1
            
            i = i + 1 
            j = j + 1
            steps = steps - 2

        if n % 2 == 1:
            result.append(matrix[n//2][n//2])

        
        return result



Q Given Matrix of size m * n print spiral 

- when we are printing outer boundery no of steps are not same 
- row and column both are changing 
- here ROW and col both are of diff 
- so we need to keep track row_steps and col_steps both 
- rather then steps here we will have now row_steps and col_steps and every tine it will be decreased by 2

- Track how many rows and columns are left to process:

    - row_steps = n (rows remaining)
    - col_steps = m (columns remaining)

- Each loop:

    - Move right for (col_steps - 1) steps
    - Move down for (row_steps - 1) steps
    - Move left for (col_steps - 1) steps
    - Move up for (row_steps - 1) steps

After finishing a ring:

    - Move inward (i += 1, j += 1)
    - Shrink the problem size (row_steps -= 2, col_steps -= 2)

At some point, either:

    - row_steps == 1 → only one row is left
    - col_steps == 1 → only one column is left

So after the main loop, we handle leftovers:

    - Traverse the remaining row left→right
    - Traverse the remaining column top→bottom

This ensures all elements are covered.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        i = j = 0 
        result = list()
        steps = n 

        row_steps = n 
        col_steps = m 
        
        while row_steps > 1 and col_steps > 1:

            for k in range(col_steps-1):
                digit = matrix[i][j]
                result.append(digit)
                j = j + 1
            
            for k in range(row_steps-1):
                digit = matrix[i][j]
                result.append(digit)
                i = i + 1
            
            for k in range(col_steps -1):
                digit = matrix[i][j]
                result.append(digit)
                j = j - 1
            
            for k in range(row_steps-1):
                digit = matrix[i][j]
                result.append(digit)
                i = i - 1
            
            i = i + 1 
            j = j + 1
            col_steps = col_steps - 2
            row_steps = row_steps - 2

        if row_steps == 1:
            for _ in range(col_steps):
                result.append(matrix[i][j])
                j += 1
        
        # leftover column
        elif col_steps == 1:
            for _ in range(row_steps):
                result.append(matrix[i][j])
                i += 1

        
        return result
        
