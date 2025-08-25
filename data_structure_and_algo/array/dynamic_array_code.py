class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.arr[i]
        raise IndexError("Index out of bounds")

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.arr[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.arr[self.size]
        raise IndexError("Cannot pop from an empty array")

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity