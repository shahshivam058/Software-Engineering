class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Push value onto stack and update min tracking."""
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Remove top element. Raises error if stack is empty."""
        if not self.stack:
            raise IndexError("Pop from empty stack")
        removed = self.stack.pop()
        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """Return top element. Raises error if stack is empty."""
        if not self.stack:
            raise IndexError("Top from empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        """Return current minimum. Raises error if stack is empty."""
        if not self.min_stack:
            raise IndexError("Min from empty stack")
        return self.min_stack[-1]
