"""
Given an Integer Numrow represents the number of rows 

That belong to pascal triangle 

5 : Build Pascal Triangle with 5 row 

In pascal Triangle each Nymber is sum of 2 number directly above it 

First array 1 
Next Array : starting and ending always 1 
each row below would be value on both diff sides above remaining values we have to calculate 
for each row will be +2 size of above row and and last and we assume that values are 0 

        [1]
       [1, 1]0
    00[1, 2, 1]0
    0[1, 3, 3, 1]0
    [1, 4, 6, 4, 1]

how we gonna compute this value 
we use 2 pointer approch 
both pointer going on same direction both are going in 

most efficient -takes time complexity of 0(n2)
we build temp row and we compute upon that one 


pascale Triangle 2 :
kind of previous one 
Given an row index return row indexth row 
Dont think about parent point of view 

"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] # base case where first row aleasys 1
 
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0] # we are building a temp array appending 0 in first and last makes computation easy for us 
            row = []
            for j in range(len(res[-1]) + 1): # each new row will be previous + 1 size so 
                row.append(temp[j] + temp[j+1]) # use temp array to compute 
            res.append(row)
        
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            # Each new row is one element longer than the previous row.
            # Start with all zeros (so you can accumulate sums in place).
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j + 1] += res[j]
            """
                For each number in the current row (res[j]):
                    Add it to the same index in next_row.
                    Add it also to the next index in next_row.
                This mimics the rule:
                    res[j] contributes to next_row[j] (left child).
                    res[j] also contributes to next_row[j+1] (right child).
            """
            res = next_row
        return res