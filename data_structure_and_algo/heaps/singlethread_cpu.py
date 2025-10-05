"""
The CPU follows these rules:

It can only process one task at a time.
Tasks must be processed in the following order:
Availability: Only tasks whose enqueue time (enqueueTime i) is less than or equal to the current CPU time are considered.
Priority: Among all available tasks, the CPU selects the one with the shortest processing time (processingTime i).
Tie-breaker: If there's a tie in processing time, the task with the smallest original index is chosen.

When a task is finished, the CPU immediately starts the next selected task. If no tasks are available, the CPU sits idle until the next task becomes available.




1. The Min-Heap Structure and Priority
The heap stores all tasks that have been "enqueued" (i.e., their enqueueTime has passed) but haven't been processed yet.

Heap Element: (processingTime i ,originalIndex i)

Ordering: It is a Min-Heap, meaning the element with the smallest value is always at the root (the top) and is the next one to be processed.
The heap prioritizes the processing time first.
If two tasks have the same processing time, the heap naturally uses the original index as the tie-breaker, since it's the second element in the tuple.

This structure directly translates the scheduling rules into an efficient data structure: select the task with the minimum processing time, then minimum index.


2. The Two-Step Process
The overall simulation involves two main stages, where the heap acts as the bridge between the sorted list of all tasks and the final output order.

Step 1: Loading Tasks (The "Feeder")
As the current_time advances, we continuously check the list of all tasks (which was initially sorted by enqueueTime).

Action: When a task's enqueueTime is less than or equal to the current_time, we push (processingTime,originalIndex) onto the heap.

Role of Heap: It serves as the waiting room for tasks the CPU can run. Loading is O(logN) per task added.

Step 2: Processing Tasks (The "Selector")
Whenever the CPU is free, it must choose the next task from the waiting room (the heap).
Action: We pop the top element from the min-heap.
Role of Heap: The pop operation is guaranteed to return the task that satisfies the selection criteria (min processing time, min index). This is the key efficiency gain, as we avoid searching through an unsorted list of available tasks. This operation is O(logN).



"""


import heapq
from typing import List

class Solution:
    """
    Implements the single-threaded CPU scheduling algorithm using a min-heap.

    The algorithm simulates the CPU's operation:
    1. Tasks are initially sorted by their enqueue time.
    2. A min-heap manages tasks that are currently available, prioritizing 
       (processingTime, originalIndex).
    3. The CPU advances time, loading available tasks into the heap, and 
       then processing the highest-priority task from the heap.
    """
    def orderTasks(self, tasks: List[List[int]]) -> List[int]:
        # 1. Preprocessing: Add the original index to each task.
        # Task format: [enqueueTime, processingTime, originalIndex]
        indexed_tasks = []
        for i, (enqueue_time, processing_time) in enumerate(tasks):
            indexed_tasks.append((enqueue_time, processing_time, i))

        # 2. Sort all tasks primarily by their enqueue time.
        # This allows us to load tasks into the CPU's queue in the order they arrive.
        indexed_tasks.sort()

        # Variables for simulation
        result = []
        # Min-heap stores available tasks, prioritized by (processingTime, originalIndex)
        available_tasks_heap = []
        
        # current_time tracks when the CPU finishes the current task.
        current_time = 0
        
        # Pointer to the next task in the sorted list to check for availability.
        task_pointer = 0
        n = len(indexed_tasks)

        # Main simulation loop runs until all tasks are processed
        while len(result) < n:
            
            # A. Load Available Tasks into the Heap
            # Check tasks that have arrived (enqueueTime <= current_time)
            while task_pointer < n and indexed_tasks[task_pointer][0] <= current_time:
                enqueue_time, processing_time, original_index = indexed_tasks[task_pointer]
                
                # Heap element format: (processingTime, originalIndex)
                # This ensures correct prioritization: shortest duration, then smallest index.
                heapq.heappush(available_tasks_heap, (processing_time, original_index))
                task_pointer += 1

            # B. CPU Processing Logic
            if available_tasks_heap:
                # CPU is not idle. Process the highest priority task (shortest processing time).
                processing_time, original_index = heapq.heappop(available_tasks_heap)
                
                # Add the task's index to the result order
                result.append(original_index)
                
                # Advance the current time by the task's processing duration
                current_time += processing_time
            else:
                # CPU is idle (heap is empty).
                # Move time forward to the enqueue time of the next arriving task.
                if task_pointer < n:
                    current_time = indexed_tasks[task_pointer][0]
                
                # If task_pointer is n, the loop will terminate, but this handles 
                # any gap between the last finished task and the next task arrival.

        return result

# --- Example Usage for Testing ---
# tasks = [[1,2],[2,4],[3,2],[4,1]]
# solver = Solution()
# print(f"Processing Order: {solver.orderTasks(tasks)}") # Expected: [0, 2, 3, 1]

# tasks_2 = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# solver_2 = Solution()
# print(f"Processing Order 2: {solver_2.orderTasks(tasks_2)}") # Expected: [4, 3, 2, 0, 1]
