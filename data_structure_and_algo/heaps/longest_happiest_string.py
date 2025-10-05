"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
You are given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.



we have to greedy here 
start with one which has max freq 
Least one which has fewer 
we should not have any char 3 times in consucative +

we gonna look at char which has highest freq 
once we done with 2 add another char and 

first always go with char which has highest freq then add another char 


"""

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        # Maintain freq in max heap allows us to get char with max freq everytime 
        for count , char in [(-a , 'a') , (-b , "b") , (-c , "c")] :
            if count != 0 :
                heapq.heappush(maxHeap , (count , char))
        

        while maxHeap :
            count , char = heapq.heappop(maxHeap)
            # check if 3 char are same which we should not if even if its there then we have to skip char and gose to next but what if heap doesnt countain char anymore 
            if len(res) > 1 and res[-1] == res[-2] == char :
                if not maxHeap :
                    break 
                count2 , char2 = heapq.heappop(maxHeap)
                res = res + char2 
                count2 = count2 + 1
                if count2 :
                    heapq.heappush(maxHeap , (count2 , char2))
                heapq.heappush(maxHeap , (count, char))
            
            else :
                count = count + 1
                res = res + char
                if count : 
                    heapq.heappush(maxHeap , (count , char))
        
        return res 
            



        