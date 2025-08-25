arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,9 , 10]
k = 3 

def sliding_window(arr , k) :
    result = 0 
    n = len(arr)
    
    # we are adding sum of first k elements
    for i in range(k) :
        result = result + arr[i]

    for i in range(k , n) : # starting looping from k to n allows us to go forward and add a new element 
        result = result - arr[i - k] # removing the contribution of first element in window 
        result = result + arr[i] # adding a current element 

    return result


# print(sliding_window(arr , k))

def find_min_length_subarray_with_sum(arr, target_sum):
    """
    Finds the minimum length of a contiguous subarray whose sum is greater than
    or equal to a given target_sum. This serves as a generic example of a
    dynamic size sliding window.

    The window dynamically expands by moving the 'window_end' pointer and
    contracts by moving the 'window_start' pointer based on the condition.

    Args:
        arr: The input list of numbers.
        target_sum: The target sum to check against.

    Returns:
        The minimum length of the subarray, or 0 if no such subarray exists.
    """
    # Initialize the pointers for the window's start and end
    window_start = 0
    # Keep track of the sum of elements within the current window
    current_sum = 0
    # Initialize the minimum length found so far to a large value
    min_length = float('inf')
    
    # Iterate through the array with the 'window_end' pointer, expanding the window
    for window_end in range(len(arr)):
        # Add the next element to the window sum
        current_sum += arr[window_end]
        
        # This is the core 'dynamic' part: while the condition is met,
        # we shrink the window from the left to find a potential smaller valid window.
        while current_sum >= target_sum:
            # We have found a valid window, so we update our result
            min_length = min(min_length, window_end - window_start + 1)
            
            # Now, we shrink the window by subtracting the element at 'window_start'
            # and moving the 'window_start' pointer forward.
            current_sum -= arr[window_start]
            window_start += 1
            
    # If min_length remains at infinity, no valid subarray was found
    if min_length == float('inf'):
        return 0
    else:
        return min_length

# --- Example Usage ---

# Example 1: A valid subarray exists
arr1 = [2, 1, 5, 2, 3, 2]
target1 = 7
result1 = find_min_length_subarray_with_sum(arr1, target1)
print(f"Array: {arr1}, Target Sum: {target1}")
print(f"Minimum length of the subarray is: {result1}")
print("-" * 30)



