"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Time can go in only single direction so you can buy in future and sell in pass 

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



The Two-Pointer Concept

The two-pointer approach involves using two pointers, a left pointer (L) and a right pointer (R), that traverse the array.

The left pointer (L) represents the potential buy day. Its purpose is to always point to the lowest price seen so far. when we found a new element change l 

The right pointer (R) represents the potential sell day. It iterates through the array, effectively scanning for the best day to sell.


Day 1 price = 7 
Day 2 Price = 1 





maximum profit we can make by buying at minimim and sell at maximum 

7 - 1 will not work we cant go back in time time gose in single direction 

we will use 2 pointer approch 

we will check what is the current profit 

L = Day we buy 
R = Day we sell 

when our R > L we will update our left 

we are using slow fast pointer approch 


when we found appropriate the element we change the slow pointer fast changing everytime search for better element 


Initialize Variables:

min_price: This variable will store the minimum price of the stock encountered as you iterate through the list. Initialize it to a very high number (like infinity) to ensure the first price in the list is always lower.

max_profit: This variable will store the maximum profit found so far. Initialize it to 0, as you can't make a negative profit in this scenario (you can always choose to not trade).

Iterate Through the Prices:

Go through each price in the prices list.

Update min_price: Check if the current price is lower than the min_price you've seen so far. If it is, update min_price to the current price. This ensures you're always buying at the lowest possible point before a potential sale.

Calculate Potential Profit: Calculate the profit you would make by selling at the current price using the lowest price you've found so far: profit = current_price - min_price.

Update max_profit: Compare this profit with your max_profit. If the calculated profit is higher, update max_profit to this new value.

Analogy
Imagine walking down a street with stock prices written on a timeline. You have two hands: one holds a sign with the lowest price you've ever seen (min_price), and the other holds a sign with your best profit so far (max_profit).

As you walk, you look at the price for the current day.

First, you look at your "lowest price" sign. If the current price is lower, you update your sign with this new, lower price. You are essentially "buying" the stock on this day.

Then, you calculate the profit you would make if you sold the stock today, using the lowest price you've ever seen.

Finally, you look at your "best profit" sign. If today's potential profit is higher, you update that sign.

You continue this process until you reach the end of the street. The value on your "best profit" sign is the answer.


"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        R = 1 
        maximum_profit = 0 

        while R  < len(prices) :
            if prices[L] > prices[R] :
                L = R 
            else :
                profit = prices[R] - prices[L]
                maximum_profit = max(maximum_profit , profit )
            
            R = R + 1
        
        return maximum_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0 

        n = len(prices)

        for i in range( 1 , n):
            min_price = min(min_price , prices[i])
            profit = prices[i] - min_price
            max_profit = max(profit , max_profit)
        
        return max_profit