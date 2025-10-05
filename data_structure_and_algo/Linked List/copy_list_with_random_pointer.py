"""
We have a linked list and each node has extra pointer named random pointer which might point any random node available in linked list 
apart from next also it has random pointer 
we have to create a deep copy of linked list 
The issue with random pointer 
node can point to node before that or node can point to another node in right 


solution will be in two pass :
1st pass create a new nodes 
1st node also gonna create a hashmap where we map orignal node to new node 
2nd pass :
all poiters connecting utilise the hashmap to map old node to new node 


it can be solved in linear time  linear space 


Just utilise the hashmap store all node with their copy in hashmap in first pass 

2nd pass go through existing linkedlist 
use hashmap for creating new 
some node might point to none so create a object none = none 


"""



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]