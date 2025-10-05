class min_heap :
    def __init__(self , arr):
        self.heap = arr
    
    def heapify_down(self , index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        
        if smallest != index :
            self.heap[index] , self.heap[smallest] = self.heap[smallest] , self.heap[index]
            self.heapify_down(smallest)
    
    def heapify_up(self , index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent] , self.heap[index] = self.heap[index] , self.heap[parent] 
            self.heapify_up(parent)
    
    def build(self) :
        n = len(self.heap)
        index = (n // 2) - 1
        while index >= 0 :
            self.heapify_down(index)
            index -= 1
        
    
    def get_min(self):
        if self.heap:
            return self.heap[0]
    
    def insert(self , val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
    
    def delete(self) :
        if self.heap :
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(0)

arr = [7 , 3 , 1,9,10,50]
heap = min_heap(arr)
heap.build()
print(heap.heap)

