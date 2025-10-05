"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and a integer array trips where trips[i] = [numPassengers[i], from[i], to[i]] indicates that the ith trip has numPassengers[i] passengers and the locations to pick them up and drop them off are from[i] and to[i] respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.


The goal is to return True if we able to process all elements else false 
go from left to right and check how many passengers we have at current point of time 
we have to keep track if current number of passangers 
Let's use a variable currentPassengers to track the count of people in the car, initialized to 0.

Sort Trips: Sort the trips array by the pickup location from i : Trips sorted by from  i
​Iterate Through Sorted Trips: For each trip [numPassengers,from,to]:
Drop-off Existing Passengers: Before picking up new passengers at the current from location, check the heap. While the heap is not empty AND the earliest drop-off location (the heap's minimum element) is ≤ the current from location:
Remove the drop-off event from the heap.
Subtract the dropped-off passengers from currentPassengers.
Check Capacity (Pickup): After dropping off all possible passengers, check if you have space for the new ones:
Add the current trip's numPassengers to currentPassengers.
If currentPassengers > capacity, return false.
Schedule Drop-off: Add the current trip's drop-off event to the heap: (to,numPassengers).
Final Result: If you iterate through all the trips without ever exceeding the capacity, return true.



"""


import heapq
from typing import List, Tuple

def carPooling(trips: List[List[int]], capacity: int) -> bool:
    """
    Determines if a car with the given capacity can complete all trips
    using a Min-Heap (Priority Queue) to track drop-off times.

    The time complexity is O(N log N) due to sorting and heap operations,
    where N is the number of trips. The space complexity is O(N) for the heap.

    Args:
        trips: A list of trips, where each trip is [num_passengers, from_location, to_location].
        capacity: The maximum number of passengers the car can hold.

    Returns:
        True if all trips are possible, False otherwise.
    """
    
    # 1. Sort the trips by the pickup location (from_location).
    # This ensures we process events in chronological order of pickups.
    # The default sort on a list of lists works on the first element, which is the 
    # number of passengers, so we must specify the key for sorting.
    # However, since the pickup location is the second element (index 1), we use lambda.
    trips.sort(key=lambda x: x[1])

    # min_heap will store (drop_off_location, num_passengers).
    # The heap is ordered by drop_off_location (the first element of the tuple).
    # This allows us to quickly find which passengers should be dropped off next.
    drop_offs: List[Tuple[int, int]] = []
    
    current_passengers = 0
    
    # 2. Iterate through the sorted trips.
    for num_passengers, pickup_location, drop_off_location in trips:
        
        # 3. Handle Drop-offs (Remove passengers who have reached their destination)
        # Check the heap: while the car has arrived at or passed an existing drop-off location,
        # passengers must exit the car.
        while drop_offs and drop_offs[0][0] <= pickup_location:
            
            # The earliest drop-off location and the number of people to drop off.
            earliest_drop_off_location, passengers_to_drop = heapq.heappop(drop_offs)
            
            # Reduce the passenger count
            current_passengers -= passengers_to_drop
        
        # 4. Handle Pickup
        # Add the new passengers to the car.
        current_passengers += num_passengers
        
        # 5. Check Capacity
        # If the capacity is exceeded, the trip is impossible.
        if current_passengers > capacity:
            return False
        
        # 6. Schedule Drop-off
        # Add the new drop-off event to the heap.
        heapq.heappush(drop_offs, (drop_off_location, num_passengers))
        
    # If we successfully complete all pickups without exceeding capacity, return True.
    return True

# --- Example Usage ---

# Example 1: Should return False (capacity exceeded at location 3: 2+3=5 > 4)
trips1 = [[2,1,5],[3,3,7]]
capacity1 = 4
result1 = carPooling(trips1, capacity1)
print(f"Trips: {trips1}, Capacity: {capacity1}, Possible: {result1}")

# Example 2: Should return True (max passengers is 5, which matches capacity)
trips2 = [[2,1,5],[3,3,7]]
capacity2 = 5
result2 = carPooling(trips2, capacity2)
print(f"Trips: {trips2}, Capacity: {capacity2}, Possible: {result2}")

# Example 3: Different trip order/locations
trips3 = [[1, 2, 4], [2, 3, 5], [3, 4, 6]]
capacity3 = 6
result3 = carPooling(trips3, capacity3)
print(f"Trips: {trips3}, Capacity: {capacity3}, Possible: {result3}")

# Example 4: Edge case where a drop-off and a pickup happen at the same location.
# Pick up 5 at 0, drop off 3 at 5. Pick up 2 at 5. Total = 4. OK.
trips4 = [[5,0,5], [2,5,10], [3,5,10]]
capacity4 = 7
result4 = carPooling(trips4, capacity4)
print(f"Trips: {trips4}, Capacity: {capacity4}, Possible: {result4}")
