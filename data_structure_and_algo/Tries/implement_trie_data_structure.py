"""
208. Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

we will only have chars a to z all lower cases 


Insert :
- When we going for inserting a word in trie data structure we gonna adding char by char 
- we start with root node it will be empty child of root node we gonna add a  child of a - p 
- we are gonna add char by char and all chars are in replationship of root and chile 
- once we are done with done we gonna mark end of word 
- when we insert next time and some char are already there utilise the existing node 
- when char is not matching add a child with diff chars


Search :
- search we will be going from root to child 
- start from root node check if char exist then go below else return false 

prefix = 
    - checking for prefix 

what is diff between search and prefix :
difference between search and prefix is if we are search for a word we gonna be check if we have excet word at end of word we are gonna mark end of word as true 
if we are searching for a prefix then we dont care if particular word is full word we have inserted we just check if its exist or not we not gonna check end of word false 
and we want to check full prefix just node few char in a string 

"""


class TrieNode :

    def __init__(self) :
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root

        for char in word :
            if char not in node.children :
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root 
        for char in word :
            if char not in node.children :
                return False
            node = node.children[char]
        
        return node.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for char in prefix :
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)