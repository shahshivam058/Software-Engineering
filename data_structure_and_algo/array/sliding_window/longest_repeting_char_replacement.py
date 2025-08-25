"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4


Brute force :

try each and every combination by replacing chars 
at the end we want to maximize result 
and maximum k changes

change the char which oocure less frequently to maximize result 
we want all chars in particular window to match most comman chars 
count the oocurance of each char in window 

we are gonna take length_of_window - COUNT[B]
4 - 3 
1 = No of char in window to replace to make max result 

we just want to replace 1 char with k we can confirm no of chars to change 
we can store map of counts 
max size = 26 

left and right pointer both will point to same char 
add it to hashmap and increase right pointer
everytime we add a char to hashmap check if current window size - count < k then we need to increase the left 
when we are shrinking the window we have to remove char from hashmap  


The Main Idea: Expand and Shrink
- Imagine you're trying to find the longest substring that you can make into all the same character with at most k replacements. Instead of checking every possible substring (which would be very slow), you use a "window" that slides over the string. This window represents a potential candidate substring.
- Expand the Window: You start with a small window and expand it by moving a right pointer one step at a time. As you expand, you're greedily trying to build the longest possible valid substring. You keep track of the character frequencies inside this window.
- Check for Validity: At each step, you ask a crucial question: "Can I make the characters in my current window all the same by performing at most k replacements?" The number of replacements needed is simple: it's the total number of characters in the window minus the count of the most frequent character.
- Shrink the Window: If the number of replacements needed is greater than k, your window is invalid. This means it's too big or has too much character diversity. To fix it, you "shrink" the window from the left by moving a left pointer. You continue shrinking until the window becomes valid again.
- Update the Answer: Every time your window is valid, you update your answer with the current window's length, because it's a potential candidate for the longest valid substring.



Initialize Variables:

left = 0: The left pointer of the window.
maxLength = 0: The longest valid length found.

maxFrequency = 0: The frequency of the most common character in the current window.

frequencyMap = {}: An empty hash map to store character counts.

Expand the Window:

The right pointer iterates from the beginning of the string to the end.

For each character s[right], you update its count in the frequencyMap. If the character isn't already in the map, add it with a count of 1. Otherwise, increment its existing count.

Update maxFrequency: maxFrequency = max(maxFrequency, frequencyMap[s[right]]). This ensures you always know the count of the most frequent character in the current window.

Check for Replacements:

Calculate the number of replacements needed: (current window size) - (maxFrequency).

The window size is (right - left + 1).

The number of characters that are not the most frequent is (right - left + 1) - maxFrequency.

Shrink the Window:

If (right - left + 1) - maxFrequency > k, it means you need more replacements than k. The window is invalid.

To fix this, you must shrink the window from the left.

Decrement the count of the character at the left pointer: frequencyMap[s[left]] -= 1.

Move the left pointer one step to the right: left += 1.

This process continues until the window is valid again.

Update the Answer:

After each iteration, update maxLength = max(maxLength, right - left + 1).




"""


def character_replacement(s: str, k: int) -> int:
    """
    Finds the length of the longest substring with at most k replacements.

    This function uses a sliding window approach with a hash map to efficiently
    solve the problem in O(N) time complexity, where N is the length of the string.
    The space complexity is O(M), where M is the number of unique characters in the string,
    but it is effectively O(1) for a fixed character set like the English alphabet.
    
    Args:
        s: The input string.
        k: The maximum number of character replacements allowed.

    Returns:
        The length of the longest possible substring.
    """
    
    # Use a dictionary (hash map) to store character frequencies within the window.
    frequency_map = {}
    
    # Initialize the left pointer, maximum length found, and the maximum frequency in the window.
    left = 0
    max_length = 0
    max_frequency = 0
    
    # The 'right' pointer iterates through the string, expanding the window.
    for right in range(len(s)):
        char = s[right]
        
        # 1. Expand the window and update the frequency of the current character.
        frequency_map[char] = frequency_map.get(char, 0) + 1
        
        # 2. Keep track of the most frequent character's count in the current window.
        # We only care about the count of the single most frequent character to determine
        # how many other characters we need to replace.
        max_frequency = max(max_frequency, frequency_map[char])
        
        # 3. Check if the current window is valid.
        # A window is valid if the number of characters we need to change
        # (window length - max_frequency) is less than or equal to k.
        window_length = right - left + 1
        replacements_needed = window_length - max_frequency
        
        # 4. If the window is invalid, shrink it from the left.
        if replacements_needed > k:
            # Decrement the count of the character that is leaving the window.
            left_char = s[left]
            frequency_map[left_char] -= 1
            
            # Move the left pointer one step to the right.
            left += 1
            
        # 5. Update the maximum length found so far.
        # The window is always valid at this point (or has just been made valid).
        max_length = max(max_length, right - left + 1)
        
    return max_length
