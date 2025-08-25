"""
Leetcode : https://leetcode.com/problems/destination-city/description/


You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".


The main aim of this question identify the destination.
start from path[0][0]
it will form a graph and return the destination city it can be reached 
last city is the one which doesnt have any outgoing edge 

"""
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {p[0]: p[1] for p in paths} #we are looping over each path and compare it to dict which can help us to reduce the no of opretion 

        start = paths[0][0] # we are starting from first city  loop untill the corrasponding destination city doesnt have any other one 
        while start in mp: # we are just going till source doesnt have any destination 
            start = mp[start]
        return start