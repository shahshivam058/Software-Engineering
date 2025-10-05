class max_heap :

    def __init__(self , arr):
        self.heap = arr
    

    def heapify_down(self , index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest] :
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest] :
            largest = right
        
        if largest != index :
            self.heap[largest] , self.heap[index] = self.heap[index] , self.heap[largest]
            self.heapify_down(largest)
    
    def heapify_up(self , index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index] :
            self.heap[parent] , self.heap[index] = self.heap[index] , self.heap[parent] 
            self.heapify_up(parent)


    def build(self):
        n = len(self.heap)
        index = (n // 2) - 1
        while index >= 0 :
            self.heapify_down(index)
            index -= 1
    
    def get_max(self):
        if self.heap :
            return self.heap[0]
        
    
    def insert(self , val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
    
    def delete(self):
        if self.heap :
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(0)

    def heap_sort(self):
        # Build max heap first
        self.build()
        sorted_arr = []
        while self.heap:
            # Move current max to sorted array
            max_val = self.heap[0]
            sorted_arr.append(max_val)
            # Remove the root and fix heap
            self.delete()
        # Since we pulled max each time → descending order
        # Reverse for ascending order
        return sorted_arr[::-1]


# Example usage
arr = [7 , 3 , 1, 9, 10, 50]
heap = max_heap(arr)
sorted_arr = heap.heap_sort()
print("Sorted array:", sorted_arr)
