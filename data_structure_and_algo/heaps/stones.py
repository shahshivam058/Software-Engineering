"""
- Build the Max-Heap: Create a list where each element is the negative of a stone's weight. Then, convert this list into a heap using heapq.
  heapify(). This process ensures the two largest stones (now the two smallest negative numbers) are readily accessible.
- Simulate the Crushing Process: Use a while loop that continues as long as there are at least two stones in the heap.
Inside the loop, heappop the two smallest negative numbers from the heap. Negate them to get the actual positive weights, y (heaviest) and x (second heaviest).
Calculate the difference y - x.
If the difference is greater than zero, it means a new stone of that weight remains. Push the negative of this new weight back into the heap.
Return the Final Weight: After the loop finishes, one of two scenarios will exist:
The heap is empty, meaning all stones were crushed. In this case, the result is 0.
The heap contains exactly one stone. Its weight is the negative of the single element in the heap. Return this value.



we have a collection of stones each have a positive weights 
we can choose two haviest stone and smash them togather 
if x == y destroy 
if x !=  y : smaller one destroy  and stone of weight y = y - x

at the end only one stone will be left return weight of stone or 0 can be possible 


we just need to simulate best thing we can do 

everytime we have to get two heaviest stone and smash them togather 

Utilise the max heap we can get the large 
using max heap we can get the max number everytime 


(nlogn)


python doesnot have maxheap we have to use min heap 


we want to simulate untill we have atleast 1 stone 
we mainly have 2 different condition 
x == y :remove both in below we are using heap to get both so both are removed heap we are not doing anything 
x != y : in this case we are removing the smaller one 

so when we are fetching largest and secound largest from heap we check 
we are comparing and adding the value to stones 
we just need to add one stone 

largest - smaller value 


if exist then return else return 0 

"""



import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)


        while len(stones) > 1 :
            y  = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y > x :
                heapq.heappush(stones , -(y - x))

        return -stones[0] if stones else 0