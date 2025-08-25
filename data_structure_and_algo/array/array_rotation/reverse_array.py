def reverse_array(arr) :
    start = 0 
    end = len(arr) - 1

    while start < end :
        arr[start] , arr[end] = arr[end] , arr[start]
        start = start + 1
        end = end - 1
    
    return arr

arr = [1 , 2 , 3 ,4 , 5]
print(reverse_array(arr)) 



"""
Initialize Pointers:

    left pointer starts at index 0 (beginning of array)
    right pointer starts at index n-1 (end of array, where n is array length)

Swap Elements:

    Swap elements at left and right positions
    Move left pointer forward (increment by 1)
    Move right pointer backward (decrement by 1)

Termination Condition:
    Continue until left pointer is no longer less than right pointer
    For even-length arrays: pointers cross
    For odd-length arrays: pointers meet at middle element



Edge Cases to Consider

Empty Array:

    Should return empty array
    Pointers won't enter while loop (left=0, right=-1)

Single Element Array:

    Should return the same array
    Pointers equal (left=0, right=0) so no swap occurs

Even vs. Odd Length:

    Algorithm handles both cases naturally
    For odd length, middle element remains in place




Practical Applications
Palindrome Checking:
    Reverse and compare with original
    Or use two pointers moving toward center
Rotating Arrays:
    Reverse portions as part of rotation algorithm
In-place Operations:
    When you need to modify array without extra space
String Manipulation:
    Reversing words in a sentence
    Reversing substrings



"""