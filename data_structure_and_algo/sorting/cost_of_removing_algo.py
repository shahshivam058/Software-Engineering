"""
The cost of each removal is the sum of all elements currently present in the array.

We want cheaper removals later, so remove larger elements first (they contribute more to the sum).
Thus, sort the array in descending order and remove elements in that order.



Sort array A in descending order.
Initialize total_cost = 0.
For each element, add the sum of current array to total_cost.
Remove the first element and repeat.


"""

def min_removal_cost(A):
    A.sort(reverse=True)
    total_cost = 0
    for i, val in enumerate(A):
        total_cost += (i + 1) * val
    return total_cost

arr = [2,4,6,7]

# 2 + 4 + 6 + 7 = 19
# 2 + 4 + 6 = 12 + 19 = 31
# 2+ 4 = 31 + 4 +2 = 37
# 2 = 39

cost = min_removal_cost(arr)
print(cost)