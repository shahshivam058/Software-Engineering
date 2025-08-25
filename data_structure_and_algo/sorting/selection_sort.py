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
Imagine you have a deck of unsorted playing cards face up on a table.
Find the smallest: You scan through all the cards and pick out the card with the smallest value.
Place it first: You place this smallest card at the very beginning of a new, sorted pile.
Repeat: You then look at the remaining unsorted cards, find the smallest among them, and place it next in your sorted pile. You continue this process until all cards are moved to the sorted pile.




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
        for j in range(i+1 , n) :
            if arr[j] < arr[min_index]: # by change to > we can sort in decreasing order 
                min_index = j 
        
        arr[i] , arr[min_index] = arr[min_index] , arr[i]

        # if min_index != i: we can avove un nessecary swaps where element is already at correct location 
        #     arr[i], arr[min_index] = arr[min_index], arr[i]


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