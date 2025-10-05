"""
We got a range in linked list 
left and right 
reverse that part of linked list 

Use the dummy node 
not part of list 
insert at begaining 
not need to hanele edge case 
we have to change between l to r 
reach l - 1 



Algorithm Steps
This task is typically solved in three main phases:
Traverse to the Start Node: Find the node preceding the section to be reversed and the node where the reversal starts.
Reverse the Sublist: Use an iterative approach (like the standard linked list reversal) to reverse the nodes from m to n.
Connect the Sublist: Reconnect the reversed sublist back into the original list structure.



1. Traverse and Setup
Create a dummy node and set its next to the list head.
Initialize a pointer, prev_m, to the dummy node. This pointer will ultimately point to the node before the mth node.
Traverse prev_m forward m−1 steps. After this loop, prev_m is at the node before the reversal starts.
Identify the start node of the reversal, start_m, which is prev_m.next. This node will become the tail of the reversed sublist.
Identify the node immediately following the sublist, end_n_next, which is start_m.next. This is the first node that will be moved during the reversal.


Use the standard iterative reversal technique to reverse the n−m edges. The reversal happens in place between the m 
th and nth nodes.

Iterate n−m times (this is the number of moves/reversals needed).

In each iteration:
Store the next node: temp = end_n_next.next.
Reverse the current node's pointer: end_n_next.next = start_m.
Move the start_m pointer back one step: start_m = end_n_next.
Advance end_n_next to its original next position: end_n_next = temp.

The key to reconnection is that before the reversal:
prev_m pointed to start_m.
start_m (the original m th node) pointed to end_n_next (the original (m+1) 

After the reversal:

The original m th node (start_m) is now the tail of the reversed section. It must point to the node immediately after the reversed section (end_n_next).

prev_m must now point to the new head of the reversed section, which is the node currently pointed to by start_m (which was the original n 
th node).

Connect the tail: start_m.next = end_n_next. (The original m th node points to the (n+1) th node).

Connect the head: prev_m.next = start_m. (The node before m points to the new head, which is the original n 
th node).

Return dummy.next as the new head of the list.


"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Implements the logic to reverse a linked list sublist between positions m and n.
    Uses the three-phase approach: Traverse, Reverse, Reconnect.
    """
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        Reverses the nodes of the list from position 'left' to 'right'.

        Args:
            head: The head of the linked list.
            left: The starting position (1-indexed).
            right: The ending position (1-indexed).

        Returns:
            The head of the modified linked list.
        """
        if not head or left == right:
            return head

        # 1. Setup Dummy Node
        # A dummy node simplifies edge cases, especially when reversing from the head (left=1).
        dummy = ListNode(0)
        dummy.next = head

        # Pointer to the node *before* the start of the reversal (m-1 node)
        prev_m = dummy
        
        # Traverse to the node immediately before the 'left' position
        # We need to move left - 1 steps from the dummy node.
        for _ in range(left - 1):
            prev_m = prev_m.next

        # 'start_m' is the left-th node. It will become the new tail of the reversed sublist.
        start_m = prev_m.next
        
        # 'end_n_next' is the (left+1)-th node. It's the first node we will move during reversal.
        end_n_next = start_m.next

        # 2. Reverse the Sublist
        # We perform the reversal 'right - left' times.
        # This uses the iterative reversal technique to swap pointers within the sublist.
        for _ in range(right - left):
            # 1. Store the node after 'end_n_next' to prevent losing the rest of the list
            temp = end_n_next.next
            
            # 2. Reverse the pointer: make 'end_n_next' point to 'start_m' (the current head of the reversed part)
            end_n_next.next = start_m
            
            # 3. Move 'start_m' backward to the newly reversed node
            start_m = end_n_next
            
            # 4. Move 'end_n_next' forward to the previously stored 'temp'
            end_n_next = temp

        # 3. Connect the Sublist
        
        # a) Connect the original 'left-1' node (prev_m) to the new head of the reversed sublist (start_m)
        prev_m.next.next = end_n_next
        
        # b) Connect the tail of the reversed section (the original 'left' node, which is prev_m.next)
        # to the node following the reversal section (end_n_next).
        # Note: prev_m.next is still pointing to the original 'left' node.
        prev_m.next = start_m

        return dummy.next

# --- Helper Functions for Testing ---

def create_linked_list(arr):
    """Creates a linked list from a Python list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Prints the values of a linked list."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

# --- Example Usage ---

if __name__ == '__main__':
    # Input List: 1 -> 2 -> 3 -> 4 -> 5
    input_list = [1, 2, 3, 4, 5]
    head = create_linked_list(input_list)
    
    # Parameters: Reverse from position 2 to 4 (inclusive)
    LEFT = 2
    RIGHT = 4

    print("Original List:")
    print_linked_list(head)
    
    # Reverse the sublist
    solution = Solution()
    new_head = solution.reverseBetween(head, LEFT, RIGHT)
    
    print(f"\nReversing sublist from position {LEFT} to {RIGHT}:")
    print("Expected Output: 1 -> 4 -> 3 -> 2 -> 5")
    print("Actual Output:")
    print_linked_list(new_head)

    # Another Example: Reversing from the start (left=1)
    input_list_2 = [5, 4, 3, 2, 1]
    head_2 = create_linked_list(input_list_2)
    LEFT_2 = 1
    RIGHT_2 = 3

    print("\n--- Example 2 ---")
    print("Original List 2:")
    print_linked_list(head_2)

    new_head_2 = solution.reverseBetween(head_2, LEFT_2, RIGHT_2)
    print(f"\nReversing sublist from position {LEFT_2} to {RIGHT_2}:")
    print("Expected Output: 3 -> 4 -> 5 -> 2 -> 1")
    print("Actual Output:")
    print_linked_list(new_head_2)
