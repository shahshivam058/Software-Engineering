"""

Rotation of array really simple 

Brute force approch just do use nested loop 

for i in range(n) :
    temp = arr[-1]
    for j in range(1 , len(nums) - 2) :
        arr[j] , arr[j + 1 ] = arr[j + 1] = arr[j]


Array rotation is a fundamental operation that involves shifting elements of an array by a specified number of positions. This operation has wide applications in computer science, from simple data manipulation to complex algorithms in image processing and cryptography.
T

Fundamental Concepts
What is Array Rotation ?
    Array rotation means moving elements of an array in a circular fashion:
    Left rotation: In a left rotation, each element of the array is shifted one position to the left. The first element of the array moves to the last position. If you want to perform a left rotation by d positions, you'd repeat this process d times. For example, if we have the array [1, 2, 3, 4, 5] and we want to perform a left rotation by 2 positions, the result will be [3, 4, 5, 1, 2]. The elements '1' and '2' are shifted to the end of the array.
    Right rotation: A right rotation is the opposite. Each element is shifted one position to the right, and the last element moves to the first position. To perform a right rotation by d positions, you'd repeat this process d times. Using the same example, [1, 2, 3, 4, 5], a right rotation by 2 positions would result in [4, 5, 1, 2, 3]. The elements '4' and '5' are shifted to the beginning.



For array [1, 2, 3, 4, 5]:

    Left rotation by 2: [3, 4, 5, 1, 2]
    Right rotation by 2: [4, 5, 1, 2, 3]


A left rotation by k is equivalent to:
    Reverse first k elements
    Reverse remaining n-k elements
    Reverse entire array


Reversal Method for Right Rotation:
    Reverse entire array
    Reverse first k elements
    Reverse remaining n-k elements


The key change is to handle the case where the number of rotations d is greater than or equal to the array's size n. If you rotate an array by n positions, you end up with the original array. For example, rotating an array of 5 elements by 5 positions is the same as rotating it by 0 positions. Therefore, the effective number of rotations is d % n.


A minor optimization for correctness:
Before starting the reversal process, you should always update d to d % n. This ensures the algorithm works correctly regardless of how large d is. It prevents unnecessary full-array reversals and guarantees that you're only performing the necessary rotations.

Time Complexity = 
 o(n) + o(k) + o(n-k)

 o(n) = reversal of whole array 
 o(k) = reversal of k element 
 o(n - k) = reversal of remaining n - k elements 



 1. Searching in Rotated Sorted Arrays
Problem: A sorted array is rotated at an unknown pivot. Find a target element efficiently.
Example: [4, 5, 6, 7, 0, 1, 2], target 0 → Index 4.
Algorithm: Modified Binary Search (O(log N)).
Verification:

Test sorted arrays rotated at every possible pivot.

Edge cases: target at first/last index, duplicate values, full rotation (original array).

LeetCode: Search in Rotated Sorted Array

2. Checking Rotated Array Equality
Problem: Verify if two arrays are rotations of each other.
Example: [1, 2, 3, 4] and [3, 4, 1, 2] → True.
Algorithm:

Check lengths.

Concatenate array A (e.g., A = [1,2,3,4,1,2,3,4]) and search for array B.
Verification:

Test with rotated/not-rotated pairs, duplicates, empty arrays.

GeeksforGeeks: Check if arrays are rotations

3. Rotating Arrays Efficiently
Problem: Rotate an array by k positions in-place.
Solutions:

Reversal Algorithm (O(n) time, O(1) space):

Reverse entire array.

Reverse first k elements.

Reverse remaining elements.

Juggling Algorithm (O(n) time, O(1) space): Uses GCD to cycle elements.
Verification:

Test with k = 0, k = n, k > n, negative k.

Check in-place constraint (no extra array).

LeetCode: Rotate Array

4. Finding Rotation Pivot
Problem: Find the index where a sorted array was rotated.
Example: [5, 6, 7, 0, 1, 2] → Pivot at index 3 (value 0).
Algorithm: Binary Search for the smallest element.
Verification:

Test fully sorted arrays (pivot = 0), reverse-sorted arrays, single-element arrays.

5. Circular Buffer / Queue Implementation
Concept: Fixed-size queues using arrays where rotation simulates circular behavior.
Operations:

Enqueue: Insert at (front + size) % capacity.

Dequeue: Remove from front = (front + 1) % capacity.
Verification:

Test buffer overflow/underflow, wrapping around indices.

6. String Rotation Checks
Problem: Check if one string is a rotation of another.
Example: "abcde" and "cdeab" → True.
Algorithm: Concatenate string A with itself and search for B (e.g., A = "abcdeabcde", find "cdeab").
Verification:

Test empty strings, same strings, unequal lengths, non-rotated pairs.

LeetCode: Rotate String

7. Matrix Rotation
Problem: Rotate a 2D matrix by 90 degrees.
Algorithm: Layer-by-layer rotation using swaps.
Verification:

Test 1x1, 2x2, 3x3 matrices.

Verify after multiple rotations (e.g., 4 rotations = original).

LeetCode: Rotate Image





"""


def reversal_part_of_array(arr , start, end) :
    while start <= end :
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    
    return arr



def array_rotation(arr , k) :
    n = len(arr) - 1
    k = k % n

    arr = reversal_part_of_array(arr , 0 , n)
    arr = reversal_part_of_array(arr , 0 , k-1)
    arr = reversal_part_of_array(arr , k, n )
    return arr

def left_rotate_reversal(arr, k):
    n = len(arr)
    k = k % n

    reversal_part_of_array(arr, 0, k-1) # we rever the first k parts which will be go to 
    reversal_part_of_array(arr, k, n-1) # we rever the remining part in array 
    reversal_part_of_array(arr, 0, n-1) # rever the whole array

    return arr


def right_rotate_brute_force(arr, d):
    """
    Rotates an array to the right by d positions using the brute-force approach.

    Args:
        arr (list): The array to be rotated.
        d (int): The number of positions to rotate.
    """
    n = len(arr)
    # Handle cases where d is larger than the array size
    d = d % n

    for _ in range(d):
        # Store the last element in a temporary variable
        temp = arr[n - 1]

        # Shift all elements to the right by one position
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]

        # Place the stored last element at the beginning
        arr[0] = temp

    return arr

# Example Usage
my_array = [1, 2, 3, 4, 5]
rotations = 2
rotated_array = right_rotate_brute_force(my_array, rotations)
print(f"Original array: [1, 2, 3, 4, 5]")
print(f"Right rotated array by {rotations} positions: {rotated_array}")

def left_rotate_brute_force(arr, d):
    """
    Rotates an array to the left by d positions using the brute-force approach.

    Args:
        arr (list): The array to be rotated.
        d (int): The number of positions to rotate.
    """
    n = len(arr)
    # Handle cases where d is larger than the array size
    d = d % n

    for _ in range(d):
        # Store the first element in a temporary variable
        temp = arr[0]

        # Shift all elements to the left by one position
        for i in range(n - 1):
            arr[i] = arr[i + 1]

        # Place the stored first element at the end
        arr[n - 1] = temp

    return arr

# Example Usage
my_array = [1, 2, 3, 4, 5]
rotations = 2
rotated_array = left_rotate_brute_force(my_array, rotations)
print(f"Original array: [1, 2, 3, 4, 5]")
print(f"Left rotated array by {rotations} positions: {rotated_array}")

arr = [0 , 1 , 2 ,3 , 4 ,5 , 6 ,7 ,8 ,9]
print(left_rotate_reversal(arr , 3))



"""
For Left Rotation
A left rotation of an array by d positions means each element shifts d places to the left. An element originally at index i will move to a new index. To find this new index, you can use the following formula:

new_index = (original_index + d) % n

Where:

original_index is the index of the element in the rotated array that you want to find.

d is the number of left rotations.

n is the total number of elements in the array.

This formula essentially calculates how far the element at the original_index has traveled from its starting point in the original array. For example, if you want to find the element at index 2 after 3 left rotations in an array of size 5, the element currently at index 2 was originally at (2 + 3) % 5 = 0. So, the element at the rotated index 2 is the same as the element at the original index 0.

For Right Rotation
A right rotation of an array by d positions means each element shifts d places to the right. An element originally at index i will move to a new index. The formula for a right rotation is slightly different to account for negative results from subtraction:

new_index = (original_index - d + n) % n

Where:

original_index is the index of the element in the rotated array that you want to find.

d is the number of right rotations.

n is the total number of elements in the array.

The addition of n before the modulo operation ensures the result is always non-negative. For example, if you want to find the element at index 1 after 2 right rotations in an array of size 5, the element at rotated index 1 was originally at (1 - 2 + 5) % 5 = 4. So, the element at the rotated index 1 is the same as the element at the original index 4.


"""