"""
Bubble sort is a simple comparison-based sorting algorithm that repeatedly steps through a list, 
compares adjacent elements, and swaps them if they are in the wrong order. This process repeats until the list is sorted.
It's named "bubble sort" because smaller elements "bubble" to the top (beginning) of the list while larger elements sink to the bottom (end).
- Most simplest sorting algo 
- we can sort in increasing or decreasing order
- we are sorting by just sorting the adjecent element 
- compare element with next element if condi satisfy then swap else do nothing 
- in each of loop largest element will be place at the end 
- in place algo and stable sort 


- Compare each pair of adjacent elements
- If they are in the wrong order (i.e., arr[j] > arr[j + 1]), swap them
- Repeat until the array is sorted

After each pass (i), the largest remaining unsorted element moves to its correct position at the end, so:
- No need to check it again
- We shrink the inner loop range (j) each time
- we are running inner loop till n - i - 1 as this are remaining element that are unsorted so dont need to compare again 

outer loop will be one represent the no of passes 
in each one element will be at correct place 


so if we run  outer loop k time last k element will be sorted 

in case we want in increasing order we can just use arr[j] > arr[j + 1] : Largest element will be at last location at end of one pass and subsequently 
in case we want in decreasing order arr[j] < arr[j+1] in this one smallest element will be place at the end 

for optimizing more we can use a flag 
Add a flag variable (swapped) to track whether any swapping occurred during a pass.

Logic:
-    If no swap happened in a full pass → array is already sorted
-    We can exit early and skip unnecessary passes


Application and Modification Questions

- Find the k-th Largest/Smallest Element: The core idea of bubble sort is that the largest element "bubbles" up to its correct position after each pass. You can use this concept to find the k-th largest element by running the outer loop only k times.
- Sorting Linked Lists: While more complex, the same logic of comparing adjacent nodes and swapping them can be applied to a singly or doubly linked list.
- Sorting with a Custom Comparator: You might be given a problem where the sorting criteria isn't just numerical. For example, sorting an array of strings based on length or an array of objects based on a specific attribute. You would still use the bubble sort structure but replace the simple if (a > b) condition with a custom comparison function.
- Sorting a Subarray: You may be asked to sort only a specific portion of a larger array, such as sorting the elements from index i to j. The bubble sort loop would just need to be adjusted to iterate over this specific range.
- Dutch National Flag Problem: Although more efficiently solved with other algorithms, a variation of bubble sort could be used to partition an array into three parts (e.g., all 0s, then all 1s, then all 2s) by repeatedly swapping elements into their correct positions.




✅ arr[n - k] → k-th Largest Element
Let’s say:

n = 5
After k = 2 passes:
2 largest elements are at the end of the array
So the 2nd largest element is at index:
➤ n - k = 5 - 2 = 3
📍 arr[n - k] is the k-th largest element


✅ arr[k - 1] → k-th Smallest Element
If you do k passes and push the smallest elements to the front, then:
The k-th smallest will be at index:
➤ k - 1 (0-based indexing)
📍 arr[k - 1] is the k-th smallest element




The Time complexity is (N * K) 


Your if not swapped: break will trigger when the first swap happens, prematurely exiting the outer loop and leaving the array unsorted.
In many cases, the algorithm won’t fully sort the list.

"""

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):  # Outer loop runs n times
#         for j in range(0, n - i - 1):  # Last i elements are already sorted
#             if arr[j] > arr[j + 1]:
#                 # Swap elements
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# all cases o(n**2)


def bubble_sort(arr) :
    n = len(arr)

    for i in range(n) :
        swapped = False
        for j in range(n - i - 1) :  # we can write but more prefer to wriite range (0 , n - i - 1)
            if arr[j] > arr[j + 1] :
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
                swapped = True
        
        if not swapped:
            break
        
    return arr 

"""
✅ Best Case: O(n)
Only for optimized version with swapped = False
- If the array is already sorted:
- No swaps happen in the first pass
- Early exit after one pass
- So: 1 pass × (n - 1) comparisons → O(n)

⚖️ Average Case: O(n²)
- Random order array
- Every element likely needs to bubble multiple times
- Roughly n * (n-1)/2 comparisons and many swaps

❌ Worst Case: O(n²)
- Array in reverse order, like [5, 4, 3, 2, 1]
- Every pair of adjacent elements must be swapped in every pass
- Total comparisons: n * (n - 1) / 2 → O(n²)
- Applies to both standard and optimized


"""

arr = [5,3,2,7,1]
print(bubble_sort(arr))


"""
We compare and swap adjacent elements to push the largest unsorted element to the end.
But suppose the last swap happened at index k.
This means:
- All elements after index k are already in correct order (sorted).
- No need to compare those again in the next pass.

👉 So instead of looping until n - i - 1, we loop only until the last swapped index in the next iteration.

It shrinks the comparison range dynamically, especially helpful for nearly sorted arrays.

Normal Bubble Sort: Always compares up to n - i - 1
This version: Compares only until where swaps occurred
This can save many unnecessary comparisons.


In bubble sort, each pass pushes the largest remaining element toward the right.
But sometimes the array gets sorted before the full pass finishes.
The position of the last swap tells you:
Everything to the right of it is already in the correct order.
Next time, you don’t need to check beyond that index.

"""

def bubble_sort_optimized(arr) :
    n = len(arr)

    while n > 0 :
        last_swapped_index = 0 
        for i in range(1 , n) :
            if arr[i - 1] > arr[i] :
                arr[i] , arr[i - 1] = arr[i - 1] , arr[i]
                last_swapped_index = i 

        n = last_swapped_index 
    
    return arr 

print(bubble_sort_optimized(arr))


"""
⏱ Time Complexity Analysis
✅ Best Case: O(n)
Array is already sorted: no swaps → last_swapped_index = 0
Loop exits after 1 pass
✅ Just like the basic swapped optimization

⚖️ Average Case: Better than O(n²) (but still O(n²))
For many partially sorted arrays:
last_swapped_index reduces the comparison range faster than classic bubble sort
So, it performs fewer comparisons and fewer passes than regular Bubble Sort
But in worst distribution, last_swapped_index may still end up near the end
🔍 Complexity is still O(n²) in Big-O notation, but faster in practice

❌ Worst Case: O(n²)
For completely reversed array like [5, 4, 3, 2, 1]:
Every element is out of place
Swaps occur on every comparison → last_swapped_index always near the end
So still:
Comparisons ≈ n(n - 1) / 2
Swaps ≈ n(n - 1) / 2
❗ No gain over standard Bubble Sort in the worst case



"""