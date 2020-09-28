# --------------------------------------------------------------------------
# Name:        Best Time to Buy and Sell Stock
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    Example 1:
      Input: [7,1,5,3,6,4]
      Output: 5
      Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.
    
    Example 2:
      Input: [7,6,4,3,1]
      Output: 0
      Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans, dp = 0, 0
        for i in range(0, len(prices)-1):
            q = prices[i+1] - prices[i]
            dp = max(dp + q, q)
            ans = max(ans, dp)
        return ans
            
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other methods (from other submissions)
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = maxsize
        max_profit = 0
        for val in prices:
            if val < min_price:
                min_price = val
            else:
                max_profit = max(max_profit, val - min_price)
        return max_profit
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        most = 0
        if len(prices) == 0:
            return 0
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            if price - low > most:
                most = price - low
        return most
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:return 0
        ans=0
        minValue=float('inf')
        for i in prices:
            if i<minValue:
                minValue=i
            else:
                ans=max(ans,i-minValue)
        return ans
##################################################
'''
