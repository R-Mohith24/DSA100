"""
The stock span problem is a financial problem where we have a series of daily price quotes for a stock and
we need to calculate the span of stock price for all days.
You are given an array arr[] representing daily stock prices, 
the stock span for the i-th day is the number of consecutive days up to day i 
(including day i itself) for which the price of the stock is less than or equal to the price on day i. 
Return the span of stock prices for each day in the given sequence.

Input: arr[] = [100, 80, 90, 120]
Output: [1, 1, 2, 4]
Explanation: Traversing the given input span 100 is greater than equal to 100 and there are no more days behind
it so the span is 1, 80 is greater than equal to 80 and smaller than 100 so the span is 1, 90 is greater
than equal to 90 and 80 so the span is 2, 120 is greater than 90, 80 and 100 so the span is 4. So the output 
will be [1, 1, 2, 4].
"""

class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        res = [0]*n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            if stack:
                res[i] = i - stack[-1]  #stock span ==> i - j (where J is previous smaller element)
                
            else:
                res[i] = i + 1
            
            stack.append(i)
            
        return res