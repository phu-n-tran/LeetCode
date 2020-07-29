# --------------------------------------------------------------------------
# Name:        Best Time to Buy and Sell Stock with Cooldown
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Say you have an array for which the ith element is the price of a 
    given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (ie, buy one and sell one share of the stock 
    multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time 
    (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
    
    Example:
      Input: [1,2,3,0,2]
      Output: 3 
      Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold = -float("inf")
        held = -float("inf")
        reset = 0
        
        for price in prices:
            preSold = sold;
            sold = held + price
            held = max(held, reset - price)
            print(held)
            reset = max(reset, preSold)
        
        return max(sold, reset)
        
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s_i = -float('inf')
        s_o = 0
        s_o_ii = 0
        for p in prices:
            s_o, s_o_ii, s_i = max(s_o, s_i + p), s_o, max(s_i, s_o_ii - p)
            
        return s_o
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #buy where u would be if u have a stock rn
        #sell where u would be if u had a stock rn and sold it
        #frozen where u would be if
        if len(prices) == 0:
            return 0
        have0_stay = 0
        have1_stay = -prices[0]
        have0_buy = -prices[0]
        have1_sell = 0
        for i in range(1, len(prices)):
            have1_stay = max(have1_stay, have0_buy)
            have0_buy = have0_stay - prices[i]
            have0_stay = max(have0_stay, have1_sell)
            have1_sell = have1_stay + prices[i]
            
        return max(have0_stay, have1_sell)
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) > 0:
            dp = [0, -prices[0], -prices[0], 0]
        else:
            return 0
        
        for i in range(1, len(prices)):
            # print(dp)
            diff = prices[i] - prices[i-1]
            # print(diff)
            dp = [max(dp[1] + prices[i], dp[2] + prices[i]), dp[3] - prices[i], max(dp[1], dp[2]), max(dp[0], dp[3])]
        # print(dp)
        return max(dp)
'''
