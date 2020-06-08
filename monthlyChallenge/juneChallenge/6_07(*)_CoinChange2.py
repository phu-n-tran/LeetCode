# --------------------------------------------------------------------------
# Name:        Coin Change 2
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given coins of different denominations and a total amount of 
    money. Write a function to compute the number of combinations that make 
    up that amount. You may assume that you have infinite number of each kind
    of coin.

    Example 1:
        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
            5=5
            5=2+2+1
            5=2+1+1+1
            5=1+1+1+1+1
    
    Example 2:
        Input: amount = 3, coins = [2]
        Output: 0
        Explanation: the amount of 3 cannot be made up just with coins of 2.
    
    Example 3:
        Input: amount = 10, coins = [10] 
        Output: 1


    Note: You can assume that
        1. 0 <= amount <= 5000
        2. 1 <= coin <= 5000
        3. the number of coins is less than 500
        4. the answer is guaranteed to fit into signed 32-bit integer
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[1]+[0]*(amount) for _ in range(len(coins)+1)]
        
        for row in range(1, len(coins)+1):
            for col in range(1, amount+1):
                if col-coins[row-1] < 0:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-coins[row-1]]
                    
        return dp[-1][-1]
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
'''
