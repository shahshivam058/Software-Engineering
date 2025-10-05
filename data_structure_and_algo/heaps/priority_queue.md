- A priority queue is an abstract data structure where each element has a "priority." The priority of an element determines the order in which it's processed. Elements with a higher priority are served before elements with a lower priority. In cases where elements have the same priority, their order of service is determined by their arrival time.

- Python's heapq module provides an implementation of a min-heap, which serves as a foundation for a priority queue. By default, it's a min-priority queue, meaning the element with the lowest value has the highest priority and is retrieved first. You can simulate a max-priority queue by storing items as their negative values.

The heapq module in Python is a specialized library that provides functions for working with heaps. It's essentially a list that's treated as a binary heap.

- heappush(heap, item): This function pushes an item onto the heap, maintaining the heap invariant. The new item is inserted at the end and then "bubbled up" to its correct position to maintain the heap property.

- heappop(heap): This function pops and returns the smallest item from the heap. The root element (the smallest) is removed, and the last element of the heap is moved to the root. It's then "bubbled down" to its correct position to restore the heap property. This operation is analogous to dequeuing from a queue.

- heapify(list): This function transforms a regular list into a heap in linear time, O(n). It's an efficient way to initialize a heap from an existing collection of items.



import heapq 

heap = []

heapq.heappush(heap , 5)
heapq.heappush(heap , 4)
heapq.heappush(heap , 2)
heapq.heappush(heap , 9)
heapq.heappush(heap , 1)


heapq.heappop(heap)


print(heap)



To implement a max-priority queue using heapq, you can store the negative of each item's priority. This is a common and effective trick. The lowest negative value will correspond to the highest positive value, so heappop will retrieve the element with the highest priority.

import heapq

# Create an empty list to act as our max-heap
max_pq = []

# Push items with the negative of their priority
heapq.heappush(max_pq, (-3, 'task_c'))
heapq.heappush(max_pq, (-1, 'task_a'))
heapq.heappush(max_pq, (-2, 'task_b'))

print("Max-Priority Queue after insertions:", max_pq)

# Pop the highest-priority (highest original value) item
first_item = heapq.heappop(max_pq)
print("Popped item:", (-first_item[0], first_item[1]))
print("Max-Priority Queue after pop:", max_pq)
