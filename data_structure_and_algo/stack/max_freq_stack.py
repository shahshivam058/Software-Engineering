"""
The Maximum Frequency Stack, often abbreviated as "FreqStack," is a data structure that extends the standard Last-In-First-Out (LIFO) 
stack principle. Instead of popping the most recently added element, 
it's designed to pop the element with the highest frequency. 
If there's a tie in frequency, it then reverts to the standard stack behavior, popping the element that was added most recently.

This problem is a classic design question that requires a clever combination of data structures to achieve optimal time complexity 
for both push and pop operations.


The core challenge is that on a pop operation, you need to efficiently find the element with the highest frequency. 
A simple hash map to store frequencies isn't enough, because if you have multiple elements with the same highest frequency, 
you still need to know which one was pushed most recently. To handle this, a single stack isn't enough either, as you would have to scan 
it to find the most frequent element, which would be an inefficient O(N) operation.


The Solution: Combining Data Structures
The most efficient and common solution uses a combination of three data structures:
freq (Hash Map): This map stores the frequency of each element. The key is the number, and the value is its current count.
freq = {5: 3, 7: 2, 4: 1}
maxFreq (Integer): A simple variable that keeps track of the maximum frequency seen so far. This is crucial for the pop operation, as it tells you which "level" of frequency to look at.
maxFreq = 3
freqToStack (Hash Map of Stacks): This is the genius part of the solution. This map associates a frequency level with a stack of elements that have that exact frequency.
freqToStack = {1: [4], 2: [7, 5], 3: [5, 7]}
The stacks inside this map are standard LIFO stacks. The key is that elements with the same frequency are grouped together in their own stack, and because we push them as they appear, the most recently added elements will be at the top of these stacks.


push(val) Operation

When a new value is pushed, the process is straightforward:
Update freq: Increment the frequency count of the value val.
Update maxFreq: Update maxFreq to be the maximum of its current value and the new frequency of val.
Push to freqToStack: Push the value val onto the stack corresponding to its new frequency.




pop() Operation
The pop operation is where these data structures work together to achieve O(1) efficiency.
Get the element: The element to be popped is the one at the top of the stack associated with maxFreq. Let's call this element val.
Pop from the stack: Pop val from the freqToStack[maxFreq] stack.
Update freq: Decrement the frequency of val in the freq map.
Update maxFreq: Check if the stack at freqToStack[maxFreq] is now empty. If it is, it means there are no more elements with that highest frequency, so you must decrement maxFreq to look for the new highest frequency level.
Return val: Return the popped value.








"""


class FreqStack:
    """
    Implements a FreqStack using standard Python dictionaries.
    The functionality remains the same as the defaultdict version.
    """
    def __init__(self):
        # freq: A hash map to store the frequency of each number.
        self.freq = {}

        # freq_to_stack: A hash map where each key is a frequency, and the
        # value is a stack (list) of all elements with that frequency.
        self.freq_to_stack = {}

        # max_freq: A variable to keep track of the highest frequency seen so far.
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Pushes an integer onto the stack.
        """
        # Get the current frequency, defaulting to 0 if the key is not present.
        current_freq = self.freq.get(val, 0) + 1
        self.freq[val] = current_freq

        # Update the max_freq if the current value's new frequency is the highest.
        self.max_freq = max(self.max_freq, current_freq)

        # Get the list for the current frequency, defaulting to an empty list
        # if the key is not present, then append the value.
        if current_freq not in self.freq_to_stack:
            self.freq_to_stack[current_freq] = []
        self.freq_to_stack[current_freq].append(val)

    def pop(self) -> int:
        """
        Removes and returns the most frequent element in the stack.
        """
        # Get the most frequent element from the top of the stack
        # associated with the current max_freq.
        val_to_pop = self.freq_to_stack[self.max_freq].pop()

        # Decrement the frequency of the popped value.
        self.freq[val_to_pop] -= 1
        
        # Check if the stack for the max_freq is now empty.
        # If so, it means the maximum frequency has decreased.
        if not self.freq_to_stack[self.max_freq]:
            self.max_freq -= 1

        return val_to_pop
