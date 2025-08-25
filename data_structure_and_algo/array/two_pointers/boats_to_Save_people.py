"""
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit.
 Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)


The Two-Pointer Approach (Opposite Direction)
Sort the People: First, sort the array of people's weights in non-decreasing (ascending) order. This step is crucial because it allows us to easily identify the lightest and heaviest remaining people. ⚖️

Initialize Pointers: Place one pointer (left) at the beginning of the sorted array (pointing to the lightest person) and another pointer (right) at the end (pointing to the heaviest person).

Greedy Strategy: Iterate while left is less than or equal to right. In each step, we use one boat. We always place the heaviest person (people[right]) in a boat. This is the greedy part—we're trying to get the most difficult person to accommodate out of the way first.

Check for a Pair: We then check if the lightest person (people[left]) can also fit in the same boat with the heaviest person without exceeding the limit.

If a pair is possible: if people[left] + people[right] <= limit, it means both can be in the same boat. In this case, we've successfully paired them, so we move both pointers inward (left++ and right--). This uses one boat for two people, which is the most efficient use of a boat.

If a pair is not possible: else, the heaviest person must travel alone. We use one boat for this person and move only the right pointer inward (right--). The left pointer remains where it is, because the lightest person is still waiting to be paired.




"""

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0 
        l = 0 
        r = len(people) - 1

        while l <= r :

            boats = boats + 1

            if people[l] + people[r] <= limit :
                l = l + 1
            
            r = r - 1
        
        return boats
