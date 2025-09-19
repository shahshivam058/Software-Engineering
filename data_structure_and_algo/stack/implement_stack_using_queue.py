"""
- Implement Stack Using Queue 
- stack and queue both are abstrect data structure 
- stack has one point for both add and removal of element 
- queue has diff ends for both add and removal 
- we have to implement stack using queue 
- dont rely upon implement stack opretion in 0(1) time practically its not possible 
- we cant remove from top from queue 
- We want the last pushed element to come out first (stack behavior).
- Since a queue naturally removes elements from the front, we need to move elements around when popping to simulate stack behavior.
- Push(x): Just enqueue x into q1. (Easy and efficient)
- Pop():
    - Transfer all elements except the last one from q1 → q2.
    - The last element left in q1 is the top of stack, remove it.
    - Swap q1 and q2 so that q1 always has the current stack elements.
- top()
    - Move all except last element from q1 → q2.
    - The last element left in q1 is the top, but instead of discarding it, move it back to q2.
    - Swap queues.


from queue import Queue

q = Queue()        # Create a queue

q.put(10)          # enqueue 10
q.put(20)          # enqueue 20
q.put(30)          # enqueue 30

print(q.get())     # dequeue -> 10 (FIFO)
print(q.get())     # dequeue -> 20
print(q.empty())   # False (30 still left)
print(q.qsize())   # 1


"""




from queue import Queue
class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        

    def push(self, x: int) -> None:
        self.q1.put(x)
        

    def pop(self) -> int:
        if self.q1.empty():
            return None 
        
        while self.q1.qsize() > 1 :
            self.q2.put(self.q1.get())

        top = self.q1.get()

        self.q1 , self.q2 = self.q2 , self.q1

        return top        

    def top(self) -> int:
        if self.q1.empty():
            return None 
        
        while self.q1.qsize()  > 1:
            self.q2.put(self.q1.get())

        top = self.q1.get()

        self.q2.put(top)

        self.q1 , self.q2 = self.q2 , self.q1

        return top




    def empty(self) -> bool:
        return self.q1.qsize() == 0
        