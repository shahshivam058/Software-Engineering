"""

The Stock Span Problem is a classic algorithmic challenge that involves analyzing a sequence of daily stock prices. 
The goal is to calculate the "span" for each day's price. The span on a given day is defined as the maximum number of consecutive days 
(including the current day) for which the stock price was less than or equal to the price on that day. 📈


Naive Approach (Brute Force)
The most straightforward way to solve this is with a nested loop. 
For each day, you can iterate backward from that day, counting the number of consecutive days where the price is less than or equal to the current day's price. You stop and move to the next day as soon as you find a price that is greater.

Time Complexity: O(n^2). This is because for each of the n days, you might have to check all n previous days in the worst-case scenario (e.g., if the prices are in strictly increasing order).

Space Complexity: O(1), as you only need a constant amount of extra space to store the span values.

Optimal approch :

A much more efficient way to solve this problem is by using a stack. The key insight is that for any given day, 
we need to find the first greater element to its left. 
The span is simply the difference between the current day's index and the index of that first greater element. 
If no such element exists (meaning the current day's price is the highest so far), the span is the current day's index plus one.


The stack will store indices of the days. The stack is maintained in a way that the prices at the indices it holds are in decreasing order 
from bottom to top.


Here is the general algorithm:

- Initialize an empty stack and an array to store the spans.
- The span for the first day is always 1. Push the index 0 onto the stack.
- Iterate through the rest of the prices from day i = 1 to n-1.
- For each day i, while the stack is not empty and the price at the top of the stack is less than or equal to the current day's price, pop the index from the stack.
- After the popping is done, if the stack is empty, it means the current price is the highest so far, so its span is i + 1.
- If the stack is not empty, the index at the top of the stack is the index of the nearest greater element to the left. The span is i - stack.top().
- Finally, push the current index i onto the stack.
- Repeat for all remaining days.

- Time Complexity: O(n). Although there's a while loop inside the for loop, each element is pushed onto the stack and popped from the stack at most once. This makes the overall complexity linear.
- Space Complexity: O(n) in the worst case, as the stack might hold all the indices if the prices are in a strictly decreasing order.




"""

class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        return len(self.arr) - i - 1
    
class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1 
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price , span))
        return span