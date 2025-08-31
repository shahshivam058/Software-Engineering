Q Given an array of size a of size n re arrange the array such that 
    - a[0] should go to correct position 
    - all element less then arr[0] left of array[0]
    - all elements greter then arr[0] right of arr[0]
    - No one is saying to sort either right part or left part 
    - we just want arr[0] at correct location 

Brute force approch :
sort the entire as it is 
if we sort the entire array then arr[0] will be automatically at correct location 
To Solve The question It is One of correct Solution 
TC : (N LOG N )


Idea2:

Its NOT Mandetory that all element on left of arr[0] should be sorted and all element after arr[0] should be sorted

With respect which element we have to correct data 

we will use kind of 2 pointer approch 

arr[0] where we want our element 

we can just use 2 simply pointers 
p1 and p2 

p1 points to arr[1] and p2 points to arr[n]

all element < arr[0] should be on left side of array 

if its < arr[0] then it should be on left side 

all element < arr[0] we are assuming in correct location and increasing pointer 

when we found larger element then arr[0] stop and go to p2 

check if p2 in correcy location so increasing the pointyer 


then we fould element smaller then arr[0]

now we have both pointer which doesnt meet the condition so both of them will exchange swap and then increase the pointer 

The moment we swap we check if compare with arr[0] and if correct location  and increase pointer 

everytime if p1 in correct location then increase pointer 
if not then stop 
go to p2 and check if p2 correct location if yes decrease 
when both are not at correct location swap

after all this modification how array looks like 

when we p1  and p2 both cross each swap arr[p2] with first element means arr[0]


def rearrange(arr):
    p2 = len(arr) - 1
    p1 = 1

    while p1 <= p2 :
        if p1 < arr[0]
            p1 ++
        else if p2 > arr[0] :
            p2 --
        else :
            swap (arr[p1] , arr[p2])
            p1++
            p2--
    
    swap(arr[0] , arr[p2])

Q Given an Subarray rearrange the subarray just like above 
     arr[s : e] we have to rearrange the subarray

     we have to rearrange whole subarray based on a[s] : all element < that on left all element greter then it on right 
     we dont have major change in sudocode 

we want any element at it correct location : 
Lets assume for first element in array we want it at it correct location 
check after rearrangment how array will look like element will be at correct positiom 
after partition check the array Element Pivot will be at correct location 

do the same use recursion 
for each part of array do the same 


now after running whole function all element on left are less then that number 
all number greter then that are on right 
we have to sort the entire subarray 
we can rearrange the subarray for s to e such that arr[s] gose to correct location 
now we can do is based on pivot element sort 
soft all the left part of pivot element 
sort all the right part of pivot element means subarray pivot+1 to end 

💡 The Intuition Behind Quick Sort

Imagine you have a deck of cards you want to sort. Instead of sorting them all at once, you pick one card—let's say the Queen of Hearts—and decide to put it in its correct place. You go through the rest of the deck and make two new piles: one pile of all the cards lower in value than the Queen of Hearts and another pile of all the cards higher in value.

After you've done this, you know the Queen of Hearts is now in its final, sorted position. The same logic is then applied to the two new, smaller piles of cards. You pick a new pivot card for each pile, and repeat the process of creating smaller and smaller piles until every card is in its correct place.




The Intuitive Breakdown
Choose a Pivot: First, you pick one element to be your "fence" or pivot. A simple choice is the very first element. Let's say your list is [5, 2, 8, 1, 9, 3] and your pivot is 5.

Two Pointers:

p1 starts at the very beginning (just after the pivot). Its job is to move forward and find a number that is too big (larger than the pivot).

p2 starts at the very end. Its job is to move backward and find a number that is too small (smaller than the pivot).

Find and Swap:

p1 moves forward until it finds a number that is 8. Since 8 is bigger than our pivot (5), p1 stops.

p2 moves backward until it finds a number that is 3. Since 3 is smaller than our pivot (5), p2 stops.

You have found two elements on the "wrong side." You swap them! The 8 and the 3 switch places.

Repeat: Now, p1 and p2 continue their search from where they left off.

p1 moves forward and finds 9. It's bigger than 5, so p1 stops.

p2 moves backward and finds 1. It's smaller than 5, so p2 stops.

They haven't crossed yet, so you swap the 9 and the 1.

Stop When They Cross: You repeat this process, with p1 finding big numbers and p2 finding small numbers and swapping them, until p1 and p2 cross over each other.



def partition(arr, low, high):
    """
    Partition the array around a pivot element (first element in the subarray).
    Elements <= pivot go to the left, elements > pivot go to the right.
    Returns the final index of the pivot element.
    """
    pivot = arr[low]
    p1 = low + 1
    p2 = high

    while p1 <= p2:
        if arr[p1] <= pivot:
            p1 += 1
        elif arr[p2] > pivot:
            p2 -= 1
        else:
            # Swap elements at p1 and p2
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1

    # Place pivot in its correct position
    arr[low], arr[p2] = arr[p2], arr[low]
    return p2

def quicksort(arr, low=0, high=None):
    """
    Sort the array using the quicksort algorithm.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high: # This is the termination condition. When the subarray has 0 or 1 elements (low >= high), it's already sorted, so we stop recursing.

        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# Example usage:
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [5, 3, 8, 4, 2],
        [1],
        [],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ]
    
    for i, arr in enumerate(test_arrays):
        print(f"Test case {i+1}:")
        print(f"Original: {arr}")
        quicksort(arr)
        print(f"Sorted:   {arr}")
        print()

This is where the magic happens. The partition function:
Selects a pivot (typically the first element in the subarray)
Rearranges the array so that:
All elements ≤ pivot are on the left
All elements > pivot are on the right
Returns the final position of the pivot

After partitioning, we know the pivot is in its correct final position. We then recursively apply the same process to:
The left subarray (elements before the pivot)
The right subarray (elements after the pivot)

