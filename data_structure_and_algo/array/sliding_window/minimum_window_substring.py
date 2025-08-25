"""


Core Intuition: Sliding Window
The most efficient way to solve this problem is using a sliding window approach. A sliding window is a conceptual technique that involves two pointers, left and right, which define a "window" or a subarray/substring within a sequence. You move the pointers to expand or shrink the window, typically to find a segment that satisfies a certain condition.

The intuition here is to:

Expand the window by moving the right pointer to the right, one character at a time. As you expand, you're trying to include all the characters from T.
Once the window contains all the required characters from T, you have a "valid" window.
Contract the window by moving the left pointer to the right. This is where you try to make the window as small as possible while keeping it valid. You keep shrinking until the window is no longer valid (i.e., it's missing one of the required characters from T).
You then repeat the process, expanding the window again from the new left position until it's valid, and then contracting it. You keep track of the smallest valid window you've found so far.


Step-by-Step Algorithm
To implement this, we need a way to efficiently track the character counts in both strings. A hash map (or an array, since we're dealing with ASCII characters) is perfect for this.

Step 1: Pre-process T 🗺️
First, create a hash map, let's call it char_map, to store the character counts for the string T. This gives us the target frequencies we need to satisfy.

Python

# Example for T = "ABC"
char_map = {'A': 1, 'B': 1, 'C': 1}
Step 2: Initialize Pointers and Counters
left = 0, right = 0: The two pointers defining our sliding window in S.

required_count: A counter, initialized to the number of unique characters in T. This helps us quickly check if the window is valid.

formed_count: A counter, initially 0. We'll increment this when we find a required character.

min_length: Stores the length of the smallest valid window found so far. Initialize to a very large number.

result_start_index: Stores the starting index of the minimum window.

Step 3: Expand the Window (Right Pointer) ➡️
Iterate through the string S with the right pointer. For each character s_char at S[right]:

Check if s_char is a character we need (i.e., it's in our char_map).

If it is, decrement its count in char_map.

If the count of s_char in our map becomes 0, it means we've satisfied the count for that character. We can then increment formed_count.

Step 4: Contract the Window (Left Pointer) ⬅️
After each expansion step, check if formed_count is equal to required_count. This indicates that our current window is valid—it contains all the characters from T with the correct frequencies.

If the window is valid, it's time to shrink it to find a smaller one:

Enter a while loop that runs as long as the window is valid (formed_count == required_count).

Calculate the current window length (current_length = right - left + 1).

If current_length is smaller than min_length, update min_length and result_start_index.

Now, move the left pointer to the right (left++) to shrink the window.

Check the character s_char that you're about to remove from the window (S[left]):

If s_char is a character from T, increment its count back in char_map.

If the count of s_char becomes greater than 0, it means the window is now invalid (it's missing one of the required characters). Decrement formed_count to reflect this.

The inner loop will continue to shrink the window until it becomes invalid again.

Step 5: Repeat and Return
The outer loop continues, expanding the window with the right pointer. This process of expanding and then contracting repeats until the right pointer has scanned the entire string S.

After the loop finishes, if min_length is still the initial large number, it means no valid window was found. Otherwise, the minimum window is S.substring(result_start_index, result_start_index + min_length).



"""


def minWindow(s: str, t: str) -> str:
    """
    Finds the minimum window substring of s that contains all characters of t.

    Args:
        s: The main string.
        t: The target string of characters to find.

    Returns:
        The minimum window substring, or an empty string if none exists.
    """
    if not t or not s:
        return ""

    # Count character frequencies in t
    t_counts = {}
    for char in t:
        t_counts[char] = t_counts.get(char, 0) + 1

    required = len(t_counts)
    formed = 0
    window_counts = {}

    left = 0
    min_len = float('inf')
    result = ""

    for right, char_s in enumerate(s):
        # Add the current character from s to the window's count
        window_counts[char_s] = window_counts.get(char_s, 0) + 1

        # Check if the character is in t and its count in the window
        # matches the required count
        if char_s in t_counts and window_counts[char_s] == t_counts[char_s]:
            formed += 1

        # If the window is valid, try to shrink it from the left
        while left <= right and formed == required:
            # Check if this is the new minimum length window
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len
                result = s[left:right + 1]

            # The character at the left pointer is about to be removed
            char_left = s[left]
            window_counts[char_left] -= 1

            # If the removed character was a required one, and we now have
            # fewer of them than needed, the window becomes invalid
            if char_left in t_counts and window_counts[char_left] < t_counts[char_left]:
                formed -= 1

            # Move the left pointer to the right
            left += 1

    return result
