
"""
The Core Concept 🧠
Character Counts: The foundation of the solution is tracking character frequencies. For a substring in s2 to be a permutation of s1, it must contain the same characters with the same exact frequencies. For example, a permutation of "abc" could be "bca" or "acb," but not "abb." All these valid permutations will have one 'a', one 'b', and one 'c'.
Sliding Window: We use a sliding window of a fixed size equal to the length of s1. We slide this window across s2, from left to right. At each position, the window represents a potential substring.
Frequency Comparison: The main task is to efficiently compare the character frequencies inside our sliding window with the frequencies of s1.

Step-by-Step Breakdown 🚶‍♂️
Create Frequency Maps:

First, create a frequency map (e.g., an array or a hash map) for the characters in s1. This map will be our "target" for comparison. Let's call it s1_map.
Create a second frequency map for the initial window in s2. This window will be from index 0 to len(s1) - 1. Let's call it s2_map.

Initial Check:

Compare s1_map and s2_map. If they are identical, you've found a permutation at the very beginning of s2. Return True.

Slide the Window:

Now, iterate with a right pointer from len(s1) to the end of s2.

In each step of the loop, you need to update your s2_map to reflect the new character entering the window and the old character leaving it.

Add New Character: Increment the frequency of s2[right] in s2_map.

Remove Old Character: The character at the start of the previous window is s2[right - len(s1)]. Decrement its frequency in s2_map.

An important detail: if a character's frequency drops to 0, you can remove it from the map to keep it clean.

Compare Frequencies:

After each update to the s2_map, compare it with s1_map.

If s1_map and s2_map are equal at any point, it means you've found a permutation. Return True.

Final Result:

If the loop finishes without finding a match, it means no such permutation exists in s2. Return False.


Why This is Efficient
Fixed Window Size: Because the length of a permutation of s1 must be equal to the length of s1, the sliding window can be a fixed size. This simplifies the logic.
Constant Time Updates: Instead of re-calculating the entire frequency map for the window at each step (which would be an O(N) operation inside the loop), you perform a constant-time O(1) update. You only add one character and remove one character. This makes the overall time complexity O(N), where N is the length of s2, which is very fast. The space complexity is O(M) where M is the size of the character set, which is effectively constant (e.g., 26 for lowercase English letters).








"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks if s2 contains a permutation of s1 as a substring using
        a standard Python dictionary for frequency maps.

        Args:
            s1: The string whose permutation is being searched for.
            s2: The string in which to search.

        Returns:
            True if s2 contains a permutation of s1, False otherwise.
        """
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, a permutation is impossible.
        if len1 > len2:
            return False

        # Create frequency maps for s1 and the initial window of s2.
        s1_map = {}
        s2_map = {}
        
        for i in range(len1):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        # Compare the initial window. If they match, we've found a permutation.
        if s1_map == s2_map:
            return True

        # Slide the window across s2.
        for i in range(len1, len2):
            # Add the new character entering the window on the right.
            char_to_add = s2[i]
            s2_map[char_to_add] = s2_map.get(char_to_add, 0) + 1
            
            # Remove the character leaving the window on the left.
            char_to_remove = s2[i - len1]
            s2_map[char_to_remove] -= 1
            
            # Clean up the map by removing the key if its count becomes zero.
            if s2_map[char_to_remove] == 0:
                del s2_map[char_to_remove]

            # Compare the maps. If they match, a permutation is found.
            if s1_map == s2_map:
                return True
        
        # If the loop completes without a match, no permutation was found.
        return False



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        s2_map = {}
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:
            return False
        
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        left = 0
        matches = 0
        
        for right in range(n2):
            char_right = s2[right]
            if char_right in s1_map:
                s2_map[char_right] = s2_map.get(char_right, 0) + 1
                if s2_map[char_right] == s1_map[char_right]:
                    matches += 1
            else:
                # If the character is not in s1, we skip it, but we don't clear the entire map.
                # Instead, we continue without adding to s2_map.
                pass
            
            # If the window size is larger than n1, we need to remove the left character.
            if right - left + 1 > n1:
                char_left = s2[left]
                if char_left in s1_map:
                    if s2_map[char_left] == s1_map[char_left]:
                        matches -= 1
                    s2_map[char_left] -= 1
                left += 1
            
            if matches == len(s1_map):
                return True
        
        return False