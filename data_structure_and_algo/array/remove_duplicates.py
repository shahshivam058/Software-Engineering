def remove_duplicates(arr):
    if not arr :
        return []
    
    arr.sort()
    i = 0 
    for j in range(1 , len(arr)):
        if arr[i] != arr[j] : # we are skipping the duplicate element we are checking if elemet are not same we are increaing the i and we are copying the new unique element to i 
            i = i + 1
            arr[i] = arr[j]
    
    return arr[:i+1]
    # if not arr:
    #     return []

    # arr.sort()  # Required for 2-pointer to work correctly
    # i = 0

    # for j in range(1, len(arr)):
    #     if arr[j] != arr[i]:
    #         i += 1
    #         arr[i] = arr[j]

    # return arr[:i+1]

# Example
arr = [1, 2, 2, 3, 1, 4]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4]


"""
How the Algorithm Works
Initial Check:

python
if not arr:
    return []
Handles the empty array case immediately

Returns an empty list if input is empty

Sorting:

python
arr.sort()
Sorts the array first to ensure duplicates are adjacent

This is crucial for the two-pointer technique to work

Two Pointers Initialization:

python
i = 0
i is the "slow" pointer that tracks the position of the last unique element

Starts at index 0 (first element is always unique)

Main Loop:

python
for j in range(1, len(arr)):
j is the "fast" pointer that scans through the array

Starts from index 1 (second element)

Duplicate Check:

python
if arr[j] != arr[i]:
Compares current element (arr[j]) with last unique element (arr[i])

If different, we've found a new unique element

Update and Move Pointer:

python
i += 1
arr[i] = arr[j]
Moves i forward to next position

Copies the new unique element to its correct position

Return Result:

python
return arr[:i+1]
Returns the slice containing only unique elements

i+1 because slicing is exclusive of the end index



"""