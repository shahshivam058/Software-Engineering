"""

for each string check if it is prefix or suffix of any other string on right 
for each string we are gonna check the string on right 


we can use kind of prefix tree or suffix triee


The algorithm involves the following steps:

Initialize a trie and a counter: Create an empty trie (a dictionary in Python, for example) and initialize a variable count to 0. The trie will store the combined prefix and suffix strings, and the counter will track the number of valid pairs.

Iterate through each word: Loop through the list of words. For each word, do the following:

a.  Create the combined string: Generate a new string that is a concatenation of the word, a separator character (like '#'), and the word's reverse. For example, if the word is "apple," the combined string would be "apple#elppa." The separator is crucial to distinguish the end of the prefix from the beginning of the suffix.

b.  Traverse and count: Traverse the trie using this combined string. At each node in the traversal, check if the current node has a key associated with it (indicating the end of a previously inserted combined string). The value associated with this key will be the count of how many times this specific combined string has been seen before. Add this count to your total count.

c.  Insert the combined string: After traversing and counting, insert the combined string into the trie. Increment the count at each node along the insertion path. This ensures that when you process a future word, you'll be able to count the number of times it has appeared as a prefix and suffix of previously processed words.

Return the final count: After iterating through all the words, the count variable will hold the total number of prefix-suffix pairs.


"""
from typing import List
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                if w2.startswith(w1) and w2.endswith(w1):
                    res += 1

        return res


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.count += 1

    def query(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count

def countPrefixSuffixPairs(words):
    trie = Trie()
    ans = 0
    
    for w in words:
        n = len(w)
        # check all borders
        for k in range(1, n+1):
            if w[:k] == w[-k:]:
                ans += trie.query(w[:k])
        trie.insert(w)   # store full word
    return ans



class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def search_and_count(self, word):
        node = self.root
        total_count = 0
        for char in word:
            if char not in node.children:
                return 0 # No match found
            node = node.children[char]
            total_count = node.count
        return total_count

def count_prefix_suffix_pairs_ii(words):
    trie = Trie()
    count = 0
    for word in words:
        combined_word = word + '#' + word[::-1]
        
        # Search and add existing pairs
        count += trie.search_and_count(combined_word)
        
        # Insert the combined word for future checks
        trie.insert(combined_word)
    
    return count

# Example usage:
words1 = ["a", "b", "a"]
print(count_prefix_suffix_pairs_ii(words1)) # Output: 1

words2 = ["a","a","a"]
print(count_prefix_suffix_pairs_ii(words2)) # Output: 3