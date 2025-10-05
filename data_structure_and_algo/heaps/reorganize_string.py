"""
Reorganize String :

You are given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

You can return any possible rearrangement of s or return "" if not posssible.


1. Feasibility Check (The N/2 Rule)
Before we start, we must know if a solution is possible at all. If a single character occurs too many times, we will inevitably have to place 
two of them next to each other.

The limit for the maximum frequency of any character is:

where N is the length of the string s.

Count Frequencies: Calculate the frequency of every character in s.
Check Constraint: If the frequency of any character exceeds this maximum, immediately return "".






The core of the strategy is Greedy: At any point, to maximize our chances of success, we should always place the character that is most difficult to place (i.e., the one with the highest remaining count), provided it's not the same character we just placed.

Populate: Create a Max-Heap populated with all character frequencies.

Heap Elements: Since Python's heapq is a Min-Heap, we store the negative of the frequency to simulate a Max-Heap structure:

Heap Element=(-frequency,character)

The character with the highest positive frequency will have the smallest negative value, placing it at the top of the Min-Heap.




We will build the result string iteratively, using a temporary holding variable (the "cooldown") to delay the re-insertion of the character we just used.

Variables:
result: The list (or string) being constructed.
max_heap: The priority queue holding all available characters prioritized by frequency.
prev_item: A tuple (frequency,character) representing the item placed in the previous iteration. It is temporarily put on "cooldown."


Step A: Re-insert the Cooldown Item
Before picking the next character, check if the character from the previous iteration (prev_item) still has remaining count. If it does, it's now safe to use again, so we push it back onto the max_heap.

Step B: Select the Highest Priority Item
Pop the top item, (neg_freq,char), from the max_heap. This is the most frequent character currently available, ensuring the greedy choice.

Step C: Append and Prepare Cooldown
Append char to the result string.

Update its remaining frequency: new_neg_freq=neg_freq+1 (which means the positive count decreased by 1).

Set this item as the new prev_item to wait for the next iteration: prev_item=(new_neg_freq,char).

Step D: Loop Termination
The loop continues until the heap is empty.

If the loop finishes and the length of the result string equals the length of the input string s, we have a valid rearrangement.






"""


import collections
import heapq
from typing import List

class Solution:
    """
    Rearranges the characters of a string so that no two adjacent characters are the same.
    Uses a Max-Heap (Priority Queue) and a Greedy approach to prioritize the most 
    frequent character that is currently safe to place.
    """
    def reorganizeString(self, s: str) -> str:
        import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = collections.Counter(s)
        
        # 1. Feasibility Check: 
        # A character must not appear more than ceil((N + 1) / 2) times.
        max_allowed_freq = (n + 1) // 2
        
        for count in counts.values():
            if count > max_allowed_freq:
                return ""
        
        # 2. Max-Heap Setup
        # Use negative frequency to simulate a Max-Heap.
        max_heap = []
        for char, count in counts.items():
            # Heap element: (-frequency, character)
            heapq.heappush(max_heap, (-count, char))

        result = []
        # Holds the item (neg_freq, char) placed in the previous iteration. 
        # It must wait one turn before being re-inserted into the heap.
        prev_item = None 

        # 3. Greedy Construction Loop
        # Loop continues as long as there are characters available in the heap.
        while max_heap:
            
            # A. Select the highest priority character (most frequent)
            neg_freq, char = heapq.heappop(max_heap)
            
            # Append to the result
            result.append(char)
            
            # B. Re-insert the previous item (THE CRITICAL STEP)
            # This character is now separated by 'char' and can be reused next turn.
            if prev_item is not None:
                heapq.heappush(max_heap, prev_item)
            
            # C. Update frequency and set the new cooldown item
            new_neg_freq = neg_freq + 1 # Incrementing negative frequency is decrementing positive frequency
            
            if new_neg_freq < 0:
                # If the current character still has remaining occurrences, put it on cooldown
                prev_item = (new_neg_freq, char)
            else:
                # Character is fully used
                prev_item = None
                
        # 4. Final Result Check
        # The feasibility check ensures a valid result is possible. If we 
        # successfully formed a string of length n, return it.
        return "".join(result) if len(result) == n else ""

# Example Usage:
# solver = Solution()
# print(solver.reorganizeString("aab")) # Output: aba
# print(solver.reorganizeString("aaab")) # Output: ""
