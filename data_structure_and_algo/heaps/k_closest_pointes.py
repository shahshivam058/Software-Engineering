"""
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given 
an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

identify the distance check which one is the closest 

we need to identify the k closest point 

we just need k closest point 

we looking for k so need k clostest 

we can do both using min heap and max heap 
min heap we just need to keep till k element 
we add element in this menner [ distance , x , y ]

linear time algo based on distance we want to fetch 

k log n :

we are storing all values in list 
heapify 
fetch k elements 


"""

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x , y in points :
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist , x , y])
        
        res = []
        heapq.heapify(minHeap)
        while k > 0 :
            dist , x , y = heapq.heappop(minHeap)
            res.append([x , y])
            k = k - 1
        
        return res
