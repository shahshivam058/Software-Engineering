"""

Insertion Sort is a simple, efficient comparison-based sorting algorithm ideal for small datasets or partially sorted arrays.
It builds the final sorted list one element at a time by inserting each unsorted element into its correct position within the sorted subarray. 
Pick element and place it to correct location at a time 

How It Works: A Step-by-Step Breakdown
Start from the second element: The algorithm begins with the second element (at index 1) of the array. It assumes that the first element (at index 0) is already sorted, forming a sorted subarray of size one.
Pick an element to insert: In each iteration, the algorithm takes the next element from the unsorted subarray. Let's call this element key.
Compare and shift: The key is then compared with the elements in the sorted subarray, moving from right to left. If an element in the sorted subarray is greater than the key, it's shifted one position to the right to make space for the key.
Find the insertion point: This shifting continues until an element is found that is less than or equal to the key, or the beginning of the sorted subarray is reached.
Insert the element: The key is then inserted into the empty position.
Repeat: The process repeats for all remaining elements in the unsorted subarray until the entire array is sorted.


Inserting an Element into a Sorted Array/List: Given an already sorted array/list and a new element, insert the new element into its correct position while maintaining the sorted order. This is essentially performing one "pass" of the inner loop of insertion sort.
Sorting a Partially Sorted Array: Given an array that is mostly sorted with only a few elements out of place, how would insertion sort perform? This highlights its adaptive nature.
Hybrid Sorting Algorithms (e.g., Tim Sort): Explain how insertion sort is used as a component in more advanced, hybrid sorting algorithms like Tim Sort (used in Python's list.sort() and Java's Arrays.sort()). These algorithms often use insertion sort for sorting small subarrays because of its low constant factors and adaptivity.
Maintaining a Sorted List/Stream: If you need to keep a list of elements sorted as new elements arrive (e.g., maintaining a sorted list of scores in a game, or a small priority queue), the insertion sort concept of finding the correct place and shifting can be applied.
Finding the Smallest/Largest k Elements (for small k): While heaps are generally more efficient for larger k, for very small k, you could maintain a sorted list of the k smallest/largest elements by inserting new elements into this list using insertion sort's logic and discarding the elements that fall outside the top k.
Sorting Objects with Custom Comparison: Sort an array of custom objects based on a specific attribute (e.g., sorting Student objects by grade or name). You'd use the insertion sort structure but replace the simple numerical comparison with a custom comparator function.

we are deviding array between unsorted array and sorted array 
instially arr[0] known as sorted array  and from 1 to n known as unsorted array 
so everytime we are checking element on unsorted part and place to correct location 
we are checking whether we still have sorted part and we element not at correct location 
shift element with right and decrease so we can go still sorted part we will go till begaining of array 


"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Starts from index 1 (because arr[0] is trivially sorted).
        # Iterates through all remaining elements (i = 1 to len(arr)-1).
        # - Stores the current element we want to place in the sorted portion.



        key = arr[i]
        j = i - 1
#         - Continue shifting elements **as long as**:
#               - We’re within bounds (`j >= 0`)
#               - AND the current sorted element `arr[j]` is **greater than** the `key`.

        while j >= 0 and arr[j] > key: # when we still have element on the left and  element on left > then key means we need to sort 
            # j >= 0: This ensures you haven't gone past the beginning of the array. It prevents an "index out of bounds" error.
            # arr[j] > key: This is the crucial comparison. It checks if the element at the current position (arr[j]) in the sorted subarray is greater than the key you're trying to insert.


            arr[j + 1] = arr[j]  # shift right
            # Inside the loop, this line is executed. It shifts the element arr[j] one position to the right. Think of it as opening up a spot for the key. Since arr[j] is larger than the key, it needs to move over to make way.

            j -= 1

        arr[j + 1] = key  # insert key

    return arr




# def insert_sorted(arr, num):
#     """
#     Insert a number into the sorted array using insertion sort logic.
#     """
#     arr.append(num)
#     i = len(arr) - 1
#     # Shift left while previous elements are greater than the new one
#     while i > 0 and arr[i] < arr[i - 1]:
#         arr[i], arr[i - 1] = arr[i - 1], arr[i]
#         i -= 1

# def process_stream(stream_data):
#     sorted_list = []
#     for num in stream_data:
#         insert_sorted(sorted_list, num)
#         print(f"After inserting {num}: {sorted_list}")

# # Example stream
# stream = [5, 2, 4, 3, 8, 1]
# process_stream(stream)
