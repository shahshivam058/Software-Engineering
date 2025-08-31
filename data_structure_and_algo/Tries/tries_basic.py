class TrieNode:
    """
    A node in the Trie data structure.

    Each node has a dictionary of children, mapping a character to a
    TrieNode, and a boolean flag to mark the end of a word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (Prefix Tree) implementation.

    This class supports inserting words and searching for them efficiently.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for char in word:
            # If the character is not already a child, create a new node for it.
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node to process the next character.
            node = node.children[char]
        # Mark the end of the word after the full word has been traversed.
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.

        Returns True if the word is found, False otherwise.
        """
        node = self.root
        for char in word:
            # If a character in the word is not a child of the current node,
            # the word does not exist in the Trie.
            if char not in node.children:
                return False
            # Move to the next node.
            node = node.children[char]
        # The word is found only if the last node marks the end of a word.
        return node.is_end_of_word

# --- Example Usage ---

if __name__ == "__main__":
    trie = Trie()

    print("Inserting the word 'apple' into the Trie...")
    trie.insert("apple")

    print("\nSearching for the word 'apple'...")
    is_found = trie.search("apple")
    print(f"Is 'apple' in the trie? {is_found}")  # Expected output: True

    print("\nSearching for the word 'app'...")
    is_found = trie.search("app")
    print(f"Is 'app' in the trie? {is_found}")    # Expected output: False (as 'app' was not inserted as a full word)

    print("\nSearching for a non-existent word, 'apricot'...")
    is_found = trie.search("apricot")
    print(f"Is 'apricot' in the trie? {is_found}") # Expected output: False



"""
🍎 Insertion
To insert a word like "apple" into a trie, you process the word character by character, starting from the root node.
Start at the Root: Begin with a pointer at the root node.
Iterate Through Characters: For each character in the word ("a", "p", "p", "l", "e"):
Check if the current node has a child corresponding to that character.
If YES: Move the pointer down to that existing child node. You are essentially following a shared path.
If NO: Create a new TrieNode for this character and add it as a child of the current node. Then, move the pointer to this new node.
Mark the End of a Word: Once you have processed the last character of the word (in this case, 'e'), set the is_end_of_word flag on the final node to True.


Let's walk through inserting "apple" and "app":

"apple":

Start at the root.

'a' is not a child of the root, so create a new node for 'a'. Move pointer to 'a' node.

'p' is not a child of the 'a' node, so create a new node for 'p'. Move pointer to 'p' node.

'p' is not a child of the first 'p' node, so create a new node for 'p'. Move pointer to the second 'p' node.

'l' is not a child of the second 'p' node, so create a new node for 'l'. Move pointer to 'l' node.

'e' is not a child of the 'l' node, so create a new node for 'e'. Move pointer to 'e' node.

Set the is_end_of_word flag on the 'e' node to True.

"app":

Start at the root.

'a' is a child of the root (created for "apple"), so just move the pointer to the 'a' node.

'p' is a child of the 'a' node, so move the pointer to the 'p' node.

'p' is a child of the first 'p' node, so move the pointer to the second 'p' node.

Set the is_end_of_word flag on the final 'p' node to True.
This process demonstrates how tries save space by sharing common prefixes.


"""


"""
🔎 Searching
Searching for a word in a trie is very similar to insertion. You follow the path of the word's characters from the root.

Start at the Root: Begin with a pointer at the root node.

Iterate and Traverse: For each character in the word you're searching for:

Check if the current node has a child for that character.

If NO: The word does not exist in the trie. Return False immediately.

If YES: Move the pointer down to that child node and continue to the next character.

Check the Final Node: If you successfully traverse the entire word, you have reached the final node of the path. To confirm the word exists, you must check its is_end_of_word flag.

If the flag is True, the word is in the trie. Return True.

If the flag is False, it means the path is just a prefix of another word (e.g., searching for "app" when only "apple" was inserted). Return False.

Let's walk through searching for "apple" and "apricot":

"apple":

Start at the root.

Traverse 'a' -> 'p' -> 'p' -> 'l' -> 'e'. All characters exist.

Reach the 'e' node. Check its is_end_of_word flag. It is True. Result: Found! ✅

"apricot":

Start at the root.

Traverse 'a' -> 'p'. The path exists.

Look for 'r' as a child of the second 'p' node. It does not exist. Result: Not found! ❌


"""