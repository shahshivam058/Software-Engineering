"""
A list of tasks (each represented by a capital letter A-Z).
A non-negative integer n which represents the cooldown interval: after executing a task, we must wait at least n units of time before 
executing the same task again.
We need to schedule tasks in the least number of time units such that:
Each time unit we can execute one task (or stay idle).
Same tasks must be separated by at least n intervals.
We return the minimum time units required.



The most crucial insight is that to minimize the overall time, you must always try to execute the task that appears most frequently and is currently available. By prioritizing the most frequent tasks, you ensure that they are processed quickly, giving the necessary cooldown time (n) to other instances of that same task.

A Max-Heap is the ideal data structure for this because it allows you to instantly retrieve the task with the highest remaining frequency.



The bottleneck comes from the most frequent tasks.
If a task appears many times, we need to space it out with at least n units between its executions.
Other tasks can "fill the gaps" to reduce idles.
So, we:

Frequency Count: First, count the frequency of every unique task (e.g., using a hash map).
Max-Heap: Push the frequencies of all tasks onto a max-heap. Since we want to prioritize tasks by how many times they still need to be run, the heap should be ordered by frequency, with the highest frequency at the root.
Queue for Cooldown: You need a separate data structure, typically a Queue (or a Deque), to hold tasks that are currently "on cooldown." Each item in this queue stores two pieces of information:
The remaining frequency of the task.
The time cycle when this task will be available again (i.e., when its n period expires).


vBefore picking a new task, check the cooldown queue. If the task at the front of the queue has passed its designated available time, move its frequency back to the Max-Heap.
Execute Task	If the Max-Heap is NOT empty:
1. Pop the highest frequency from the Max-Heap. This is the task we execute.
2. Decrement its frequency by 1.
3. If the remaining frequency > 0, push the task onto the cooldown queue. Its availability time will be current time t+n (the current cycle plus the cooldown period).
Idle Cycle	If the Max-Heap IS empty but the cooldown queue is NOT empty:
1. The CPU must idle.
2. You simply increment the time cycle t and proceed to the next step.
Termination	The simulation stops when both the Max-Heap and the Cooldown Queue are empty.


we utilise both queue and heap 

heap allows us to get the max freq 
queue allows us to maintain cooldown 

we remove from heap and check increase to make it 0 
if its 0 then no problem else there is another task so add to q with expected time and count 


everytime in loop check if item in queue  reach current time then add to heap again 




"""


import heapq
from collections import Counter, deque

def leastInterval(tasks, n):
    freq = Counter(tasks)
    
    # Max heap (store negative counts)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)
    
    time = 0
    cooldown = deque()  # stores (ready_time, count)
    
    while max_heap or cooldown:
        time += 1
        
        if max_heap:
            cnt = heapq.heappop(max_heap)
            cnt += 1  # since cnt is negative, this decreases frequency
            if cnt != 0:  # still have tasks left
                cooldown.append((time + n, cnt))
        
        # Check if any task is out of cooldown
        if cooldown and cooldown[0][0] == time:
            ready_time, cnt = cooldown.popleft()
            heapq.heappush(max_heap, cnt)
    
    return time
