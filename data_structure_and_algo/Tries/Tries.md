- For Using Tries we using Itrations 
- Note : 90 Percent question in tries can be solve by just just concept of search and insert in Tries 

- To Introduced Two String how much time it will take ?
    - It will Take O(N)
    - we are looping over a size of string and checking char by char 
    - Internally it is still O(N)

Q Given N Strings and Q Query for each Query Q check if it is Present in N String 

- all chars are from  a to z and size of each string is L OR < L
- N is nothing but list of string  and Q is nothing but a list of string for each query in q check if string available in N sized string list or not 

Brute force approch :
- Loop over a q query check if its exist in Strings or not 
- for each in query check in strings list 
- N words and q query : for each word compare its O(N)
- o(Q * N * N)
- We are not using any extra space O(1)

- How we can optimize 

- The main aim we need to check if q string exist in List of string or not we just need to check if there or not so hashset is enough 

Brute force 2 :

- Insert all Words In Hashset , O(N * l) We are instering the string of size l to hashset
- for each query check if exist in hashset or not 
- Time Complexity :  O(N * l) + Q * o(L)



Note : To Insert / Update / Delete A string of size l  in hashset 0(L)

The "Why": The Problem with Traditional Data Structures
Imagine you need to store a massive number of words (like for a dictionary, spell checker, or search engine autocomplete). You might consider using a Hash Table or a Balanced Binary Search Tree (BST).

While these are excellent for general-purpose storage, they have significant limitations for a specific type of operation: prefix-based searching.

Problem 1: Inefficient Prefix Searches
    Task: Find all words that start with the prefix "pre" (e.g., "prevent", "present", "premium").
    With a Hash Table: This is nearly impossible. A hash function turns a whole string into a random index. There's no way to find all words that share a common prefix without checking every single key (an O(n) operation), which is disastrously slow for large datasets.

    With a BST: You can do an inorder traversal, but you still have to check every node. It's slightly more organized but still inefficient (O(n)) for this task.
Problem 2: Wasted Space and Hashing Overhead
    Hash Tables can have collisions and require a good hash function. They also don't explicitly store the relationship between words. The words "car" and "cat" are treated as completely unrelated, even though they share a common prefix ("ca").
Problem 3: Longest Prefix Matching (a critical networking problem)
    Task: In network routers, an IP address (e.g., 192.168.21.5) must be matched to the longest matching subnet prefix in a routing table. This is incredibly cumbersome and slow with hash tables or BSTs.

The Trie (pronounced "try", from the word retrieval) was introduced to solve these exact problems. It's a tree-like data structure optimized for storing and searching sets of strings, especially where prefix relationships are key.



TO Further Optimize above we can use Tries : 
- Tries Uses The concept of TREE 
- Hierarchical Data Structure 
- N- Ary Tree - No of child nodes can be > 2 
- Everyone Uses Google DOC :
    - cricet - we dont have word - when we add a wrong word it gives us warning , Wrong Spelling , Happends In lots of case 
    - Mails , Spell Check 
    - To Check Validity of string Need to Know if word is correct or not 
    - All correct words are already stored 
    - everyword we type we check if its in correct word or not 
    - add element in Data structure : Tries 
    - Auto Complete is also implemented using Tries 
    - For each computer Auto Complete shows the same result ? No Might be 
    - Its based on how Continous we are checking data 
    - Suggestion will change from person to person 
    - Its generally use for information Retrival 
    - In Tries Data will be filled TOP Down 


- The Big Idea: Instead of storing the entire string in a node, the path from the root to a node defines the key (prefix) it represents.
- Root Node: Represents an empty string.
- Nodes: Each node (except the root) represents a single character. A path from the root traversing edges labeled c -> a -> r leads to a node that represents the word "car".
- Markers: Nodes are often marked with a boolean isEndOfWord flag to indicate that the path from the root to that node forms a complete word from the set.
- Edges: Each edge from a parent node to a child node represents a single character.
- Keys: A complete key (a word) is represented by a path from the root to a specific node. The sequence of characters on the edges along this path forms the key.
- End-of-Word Marker: To distinguish a valid key from a prefix of a longer key, a special marker or flag is often used in the node that corresponds to the end of a word. For example, if "car" and "carpet" are in the Trie, the node for "r" in "car" would have an "end-of-word" flag, while the node for "t" in "carpet" would also have one.


General Structure of Tree Node :

Node {

    DATA 
    LEFT 
    RIGHT
}

- In first of all what data we want store in Tries , We Want to store a Strings 
- Every Char = { A - Z}
- if we directly add Word for node : It will not make any change 
- Still Same 
- Rather then adding a string 
- we can add a char by char in tries 
- We may have any many distinct char as we wants 
- WE may have 26 diff root Nodes 
- Insted of creating  DIFFERENT Root Node with Distinct Char Creare a dummy node 
- All distinct chars node child of Dummy Node 
- Dummy Node might have 26 Diff child nodes 
- it might point to any char 
- each node only store char 
- each node can have upto 26 chars 
- In case java or python we are declaring array and insilizing with null 
- 


Class Node Structure for Tries :

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False



- self.children = {}: This dictionary is the core of the node's structure. It maps a character (like 'a', 'b', 'c', etc.) to another TrieNode object. For example, if you're storing the word "cat," the root node's children dictionary would have a key 'c' pointing to a new node, that new node's children dictionary would have a key 'a' pointing to another node, and so on. This structure allows for efficient prefix-based searching.

- self.is_end_of_word = False: This boolean flag is crucial for distinguishing between a node that is part of a word's path and a node that marks the end of a complete word. For instance, in a trie containing "car" and "card," the node for 'r' will have is_end_of_word set to True for the word "car," while the node for 'd' will also have it set to True for the word "card."


- Very first Node or Root Node will be dummy Node 
- 
- from dummy node 
- Very first node will be dummy node which char we want to add : D check a if d exist of not in self.children and add a d with new node as value
- when we see a new char new string we dont add in root node check in child node 
- every node will have an address 
- for each new word we will start from a root 
- insert char if not present in hashmap 
- if presents just store the current node 

- For the first question just add all  words in a trie and  just search forr it 



Enhanced Trie Node with Additional Features 


class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode mapping
        self.is_end_of_word = False
        self.word_count = 0  # Count how many words end here
        self.prefix_count = 0  # Count how many words have this prefix
        
    def __repr__(self):
        return f"TrieNode(is_end={self.is_end_of_word}, children={list(self.children.keys())})"

Questions where this form makes work easier:

- Prefix Counting: "How many words in my vocabulary start with the prefix 'un'?" You can find the node for the prefix un and simply return its prefix_count value, without having to traverse all its children. This is a very efficient operation. for each new char we will increase the count of prefix_count 

- Word Frequency (Simple): "How many times does the word 'the' appear in a large text document?" When building the trie, you increment the word_count field on the final node for the every time it is inserted. This gives you a direct count for each word. . Once we are done with traversing word we will increase the word count by 1 

- Basic Autocomplete: "Give me the number of possible word completions for the prefix 'cat'." You just need to return the prefix_count of the node corresponding to the prefix "cat".

- Unique Word Counting: "How many unique words are in a text?" You can sum the word_count fields for all nodes where is_end_of_word is True.



OR :

class EnhancedTrieNode:
    def __init__(self):
        self.children = {}          # char -> EnhancedTrieNode mapping
        self.is_end_of_word = False # Marks complete word
        self.word_count = 0         # Count of complete words ending here
        self.prefix_count = 0       # Count of words with this prefix
        self.word_frequency = 0     # Frequency/weight for ranking
        self.metadata = {}          # Additional data storage
        self.last_accessed = None   # Timestamp for LRU caching
        
    def __repr__(self):
        return f"TrieNode(end={self.is_end_of_word}, words={self.word_count}, prefixes={self.prefix_count})"

Questions where this form is necessary:

Smart Autocomplete and Search Suggestions: "When a user types 'weather', suggest 'weather forecast' and 'weather today' first because they are the most popular searches." The word_frequency field allows you to rank suggestions. Instead of just returning all words with the prefix, you can return a sorted list based on frequency, which provides a better user experience.

Comprehensive Spell Checkers and Dictionaries: "What is the definition of the word 'trie'?" You can store the definition, part of speech, and other related information within the metadata dictionary of the final 'e' node for the word 'trie'.

Router for a Web Application: "When a request comes in for /api/users/123, find the correct handler function." The metadata field can store a reference to the function that handles that specific URL route. The trie structure efficiently routes the request based on its path.

Predictive Text and Language Models: "Suggest the next word based on a given sequence." The word_frequency can be used to store probabilities of the next word appearing, which is essential for predictive text.

Caching and Memory Management: "Clean up old, unused URL routes from the trie." The last_accessed timestamp can be used to implement a Least Recently Used (LRU) caching strategy. Routes that haven't been accessed recently can be removed to free up memory.


Time Complexity :
Insert N Words And Search Q Words :
N * L + Q * L : It is faster Fastest way to search if word is there or not 

- As a space is huge westage we use hashmap insted of array of size 26
- 


Problems with this approach: If we are not starting inserting from ROOT 
- Lost common prefixes: "apple" and "application" become separate trees
- Inefficient search: Can't efficiently find all words with prefix "app"
- Wasted memory: No sharing of common prefixes
- Broken structure: Not a true trie anymore


