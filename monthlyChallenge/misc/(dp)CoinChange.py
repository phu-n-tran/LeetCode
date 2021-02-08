# --------------------------------------------------------------------------
# Name:        Coin Change (dynamic programming - bottom up approach)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given coins of different denominations and a total amount of
    money amount. Write a function to compute the fewest number of coins 
    that you need to make up that amount. If that amount of money cannot 
    be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

 
    Example 1:
      Input: coins = [1,2,5], amount = 11
      Output: 3
      Explanation: 11 = 5 + 5 + 1
    
    Example 2:
      Input: coins = [2], amount = 3
      Output: -1
    
    Example 3:
      Input: coins = [1], amount = 0
      Output: 0
    
    Example 4:
      Input: coins = [1], amount = 1
      Output: 1
    
    Example 5:
      Input: coins = [1], amount = 2
      Output: 2

    Constraints:
      1) 1 <= coins.length <= 12
      2) 1 <= coins[i] <= 231 - 1
      3) 0 <= amount <= 104
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] * (amount+1) # if amount is 2, dp will be [amount+1, amount+1, amount+1] index 0,1,and 2
        dp[0] = 0
        
        for x in range(1, amount+1):
            for each_coin in coins:
                if x - each_coin >= 0:
                    dp[x] = min(dp[x], 1 + dp[x-each_coin])
                    
        return dp[amount] if dp[amount] != (amount+1) else -1
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################

'''
