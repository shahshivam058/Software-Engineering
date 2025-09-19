"""
- Main check push and pop opretions 


Why max(len(self.s1), len(self.s2)) == 0?
We are using two stacks (s1 and s2) to simulate a queue.
At any given time:
Some elements may still be in s1 (newly pushed, not yet moved).
Some elements may be in s2 (already reversed, ready for popping/peeking).
To know if the queue is empty, we must check both stacks.
"""


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0