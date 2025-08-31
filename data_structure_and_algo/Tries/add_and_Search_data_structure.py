"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Brute force : Brute for approch is store in list and compare 

Optimal : Use Tries 
Tries is data structure where we have root node and each node may have up to max 26 childs 
each node represents single char 
we are gonna reuse the chars we inserted 
we are gonna utilize  existing node for each char saves space for us 
. means we can match any char 
we have to use deapth first search or back tracking 
what we need to check is one word which match 



while searching we gonna use index of word 

2 conditon we gonna check while looping if . char or if normal char our regular condition 
if it not gonna exist in normal we will return false 
. char will be trick 
. can match any of 26 chars 
. it can make any of child so we gonna try that 
- so we gonna do is deapth first search 
- when we gonna try with deapth first search means check if current char otherwise gonna try with remaining chars 
- when we find path return true 
- in the end return current end of word 
"""