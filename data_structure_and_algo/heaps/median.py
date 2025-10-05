"""
The Main Aim is to get median 

Median can be different for even and odd element 

in case no of elements are odd : middle element = n // 2
in case of even  elements = middle 1 + middle 2 // 2


Code will have 2 function :
Get median : median element in array 
insert : allows us to add new element

Insted of having a single list 
break it into two : Total Two subsets 


arr = [1 , 2 , 3 , 4 ]

arr1 = 1 , 2 
arr2 = 3 , 4


all element in left always less than or equal to 
all element are always greter than 

use heap data structre 

small heap : Element smaller than large heap 
large heap : element larger than small heap 

size = approximetly equal 
diff of 1 element is allowed as we have odd sized array 
if diff between >=  2

we will be using heaps the main diff is in heap :
adding element and removal 
element place based on priority 
add and removal = 0(1)

get the largest value from min heap and smallest value from max heap sum and return 

in case 

small heap = max heap 
large heap = min heap

adding and removal always log n opretion 



"""
import heapq
class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
