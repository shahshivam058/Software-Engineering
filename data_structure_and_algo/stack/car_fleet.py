"""
The core of the problem is to determine how many groups of cars (fleets) will arrive at a common destination. The rules for fleet formation are:

Single-Lane Road: Cars cannot overtake each other. A faster car will slow down to match the speed of a slower car in front of it if it catches up.
Fleet Definition: A car fleet is a single car or a group of cars traveling at the same position and speed.
Destination Point: If a car catches up to a fleet exactly at the destination, it is considered part of that same fleet.

You are given:

target: An integer representing the distance to the destination.
position: An array of integers, where position[i] is the starting position of the i-th car.
speed: An array of integers, where speed[i] is the speed of the i-th car.




The most crucial concept for solving this problem is to calculate the time it takes for each car to reach the destination. 
Since a car cannot pass the one in front of it, the only thing that matters is the arrival time.


time = target - position[i] / speed[i]



A car behind another car will form a fleet with the one in front if and only if its arrival time is less than or equal to the arrival 
time of the car in front. If its arrival time is greater, it means it will never catch up to the car in front (or the fleet in front) and will therefore form its own, separate fleet.


The most elegant and efficient solution involves two main steps:

Sort the Cars: First, you must process the cars in a meaningful order. Since fleet formation only happens with cars that are ahead of a 
given car, it's best to sort the cars by their starting position in descending order. This allows you to process the cars from the one 
closest to the destination to the one farthest away. This way, when you consider a car, you are always looking at cars that are already 
ahead of it.



Iterate and Count Fleets: After sorting, you can iterate through the cars and use a stack (or a simple variable) to keep track of the arrival times of the fleets that have formed.
For each car, calculate its arrival time to the destination.
Compare this car's arrival time to the arrival time of the last fleet to form.
If the current car's arrival time is greater than the arrival time of the last fleet, it means this car will never catch up and will form a new, separate fleet. You increment your fleet count and update the "last fleet's arrival time" to the current car's arrival time.
If the current car's arrival time is less than or equal to the last fleet's arrival time, it means it will catch up and join that fleet. You do nothing, as it doesn't form a new fleet.


The Next Greater Element problem typically involves finding the first element to the right that is greater than the current element. In the Car Fleet problem, 
the logic is inverted to work on arrival times:


We process the cars from the right-most position (closest to the target) to the left-most position (farthest from the target).
The stack stores the arrival times of the leading cars in each potential fleet. The key is to maintain a monotonic stack, but instead of finding the next greater element, we're essentially looking for the next greater or equal arrival time.
Calculate its arrival time.

Compare it to the top of the stack. The value at the top of the stack is the arrival time of the car directly in front of the current car.

If the current car's arrival time is less than or equal to the time on the top of the stack, it means it will catch up to the fleet ahead. In this case, it joins that fleet, and the top 
of the stack is no longer relevant as the new fleet's arrival time is now determined by the car that joined it.We pop the stack top to reflect this consolidation.

If the current car's arrival time is greater than the time on the top of the stack, it means the car is too slow and will not catch up. It therefore forms a new fleet. This is where the Next Greater Element analogy comes in: you've found a "greater" element (a slower car) that will start a new fleet. We push this new, greater time onto the stack.

"""
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # Stores arrival times of fleet leaders

        for p, s in cars:
            # Use floating-point division to get accurate arrival times
            arrival_time = (target - p) / s

            # If the stack is not empty and the current car's arrival time
            # is LESS THAN OR EQUAL TO the arrival time of the fleet leader
            # ahead of it (stack[-1]), it means this car will join that fleet.
            if stack and arrival_time <= stack[-1]:
                # Do nothing. The current car joins the existing fleet.
                # The leader's arrival time (stack[-1]) still determines the
                # fleet's overall arrival time.
                continue  # Skip to the next car
            else:
                # If the stack is empty or the current car's arrival time
                # is GREATER than the leader's time, it means it's a new fleet.
                # Push its arrival time onto the stack.
                stack.append(arrival_time)
        
        # The number of fleets is the final size of the stack.
        return len(stack)