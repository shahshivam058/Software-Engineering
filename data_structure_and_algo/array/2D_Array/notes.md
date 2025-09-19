A 2D array is organized conceptually into a set of rows and columns. Think of it like a spreadsheet.

Rows: The horizontal sets of elements.

Columns: The vertical sets of elements.

Elements: The individual values stored at the intersection of a row and a column. Each element is uniquely identified by two indices: one for its row and one for its column.

While we visualize it as a grid, a 2D array is stored in contiguous memory locations, similar to a 1D array. The compiler flattens the 2D structure into a linear sequence. The two common storage methods are:

Row-major order: The most common method. The elements of the first row are stored consecutively, followed by the elements of the second row, and so on. Most programming languages, like C++, Java, and Python, use this method.

Column-major order: The elements of the first column are stored consecutively, followed by the elements of the second column, and so on. This is used in languages like Fortran and MATLAB.

Understanding this storage mechanism is important for optimizing memory access and performance, especially in scientific computing.

Declaration and Initialization
The syntax for declaring and initializing a 2D array varies slightly by language.

In C++:

C++

// Declaration
int matrix[3][4]; // A 3x4 matrix (3 rows, 4 columns)

// Initialization
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
In Java:

Java

// Declaration and initialization
int[][] matrix = new int[3][4];

// Initialization with values
int[][] matrix = {{1, 2, 3}, {4, 5, 6}};
In Python:

Python



# Declaration and initialization
matrix = [[0, 0], [0, 0], [0, 0]] // A 3x2 matrix (3 rows, 2 columns)

# Initialization with values
matrix = [[1, 2, 3], [4, 5, 6]]
Python uses nested lists to represent 2D arrays.

Accessing Elements
To access or modify an element in a 2D array, you must specify both the row and column indices. The indices are usually zero-based, meaning the first row is index 0 and the first column is index 0.

To access the element in the i th row and j th column of a 2D array, you would use matrix[i][j].

For a column, you would use matrix[i][j].

For a 3x4 array named matrix, matrix[0][0] would be the top-left element, and matrix[2][3] would be the bottom-right element.



Matrix Diagonal Sum
Transpose Matrix
Image Smoother
Largest Local Values in a Matrix
Lucky Numbers in a Matrix
Magic Squares In Grid
Rotate Image
Spiral Matrix
Spiral Matrix II
Spiral Matrix III
Spiral Matrix IV
Set Matrix Zeroes
Convert 1D Array Into 2D Array
Shift 2D Grid
Rotating the Box
Minimum Operations to Make a Uni-Value Grid
Largest Submatrix With Rearrangements



Arrays & Strings: Palindrome Number, Plus One, Roman to Integer, Integer to Roman, Excel Sheet Column Title, Largest Odd Number in String, Greatest Common Divisor of Strings, Multiply Strings, Zigzag Conversion, Integer to English Words, Count Odd Numbers in an Interval Range, Count Total Number of Colored Cells, Sum of Square Numbers.

Matrices: Matrix Diagonal Sum, Transpose Matrix, Rotate Image, Spiral Matrix (I, II, III, IV), Set Matrix Zeroes, Largest Local Values in a Matrix, Magic Squares In Grid, Image Smoother, Convert 1D Array Into 2D Array, Shift 2D Grid.

Linked Lists: Insert Greatest Common Divisors in Linked List.

Math & Bit Manipulation: Power of Four, Happy Number, Ugly Number, Pow(x, n), Find the Punishment Number of an Integer, Check if Number is a Sum of Powers of Three, Minimum Number of One Bit Operations to Make Integers Zero.

Simulation & Logic: Count of Matches in Tournament, Water Bottles, Calculate Money in Leetcode Bank, Walking Robot Simulation, Robot Bounded In Circle, Find the Winner of the Circular Game.

