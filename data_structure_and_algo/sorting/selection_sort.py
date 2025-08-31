"""
selection sort :
sorting algoritham efficient than bubble sort 

1. Select the Minimum and Place at the Beginning
✅ This is the standard selection sort.
- Sorted portion grows from left to right
- You find the smallest element from unsorted and move it to the start of the unsorted section

2. Select the Maximum and Place at the End
- ✅ This is an equivalent variation of selection sort.
- Sorted portion grows from right to left
- You find the largest element and move it to the end of the unsorted portion

Core Idea and Analogy
How It Works
Selection sort divides the input list into two sublists: a sorted sublist and an unsorted sublist. Initially, the sorted sublist is empty, and the unsorted sublist contains all the elements. The algorithm proceeds as follows:
Find the Minimum: Iterate through the unsorted sublist to find the element with the smallest value.
Swap: Swap the minimum element found with the first element of the unsorted sublist. This moves the smallest element to its correct position in the sorted part of the array.
Shrink the Unsorted Sublist: The sorted sublist now grows by one element, and the unsorted sublist shrinks.
Repeat: Repeat the process with the remaining unsorted sublist until the entire list is sorted.





we are looping on array 
for each element check on right part of an array 
identify the minimum value on all right part 
place element at correct locatoion that is i 

- Find the k-th Largest/Smallest Element: The core idea of bubble sort is that the largest element "bubbles" up to its correct position after each pass. You can use this concept to find the k-th largest element by running the outer loop only k times.
- sorting an part of arry 

"""

def selection_sort_min_to_front(arr):
    n = len(arr)
    for i in range(n) :
        min_index = i 
        for j in range(i+1 , n) : # we will identify the minimum value till i and place it 
            if arr[j] < arr[min_index]: # by change to > we can sort in decreasing order 
                min_index = j 
        
        arr[i] , arr[min_index] = arr[min_index] , arr[i]

#         # if min_index != i: we can avove un nessecary swaps where element is already at correct location 
#         #     arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr





arr = [5,3,4,2,6]

print(selection_sort_min_to_front(arr))



"""
🕒 Time Complexity
Case	Reason
Best Case	Still must scan entire unsorted array to find min every time → O(n²)
Worst Case	Same logic, no matter the input order → O(n²)
Average	Still scans unsorted part each time → O(n²)


"""