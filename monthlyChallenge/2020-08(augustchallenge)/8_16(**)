# --------------------------------------------------------------------------
# Name:        Best Time to Buy and Sell Stock III
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.

    Note: You may not engage in multiple transactions at the same time 
    (i.e., you must sell the stock before you buy again).

    Example 1:
      Input: [3,3,5,0,0,3,1,4]
      Output: 6
      Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                   Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
   
    Example 2:
      Input: [1,2,3,4,5]
      Output: 4
      Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                   Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                   engaging multiple transactions at the same time. You must sell before buying again.
    
    Example 3:
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
        if len(prices)==0:return 0
        total_profit = itmd_profit = 0
        b1 = prices[0]       
        b2 = float('inf')
        
        for i in range(1,len(prices)):
            b1 = min(b1,prices[i])
            itmd_profit = max(itmd_profit,prices[i]-b1)
            b2 = min(b2,prices[i]-itmd_profit)
            total_profit = max(total_profit,prices[i]-b2)
        return total_profit
            
                
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def maxProfit(self, A):
        """
        :type prices: List[int]
        :rtype: int
        """
        a=[0 for i in range(len(A))]
        if len(A)==0:
            return 0
        m=A[-1]
        for i in range(len(A)-2,-1,-1):
            if m>A[i]:
                a[i]=max(m-A[i],a[i+1])
                
            else:
                m=A[i]
                a[i]=a[i+1]
        m=A[0]
        b=[0 for i in range(len(A))]
        for i in range(1,len(A)):
            if m>A[i]:
                m=A[i]
                b[i]=b[i-1]
            else:
                b[i]=max(A[i]-m,b[i-1])
        ans=0   
        for i in range(len(A)):
            if ans<a[i]+b[i]:
                ans=a[i]+b[i]
                
        return(ans)
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        dp_i_2_0 = 0
        dp_i_2_1 = -sys.maxint
        dp_i_1_0 = 0
        dp_i_1_1 = -sys.maxint
        for i in range(N):
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + prices[i])
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - prices[i])
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + prices[i])
            dp_i_1_1 = max(dp_i_1_1,  -prices[i])
        return dp_i_2_0
##################################################
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # A[i] = A[i-1]
        # B[i] = max(B[i-1], A[i-1] - p)
        # C[i] = max(C[i-1], B[i-1] + p)
        # D[i] = max(D[i-1], C[i-1] - p)
        # E[i] = max(E[i-1], D[i-1] + p)
        if len(prices) == 0:
            return 0 
        A, B, C, D, E = 0, -prices[0], float('-inf'), float('-inf'), float('-inf')
        for i in range(1, len(prices)):
            A, B, C, D, E = A, max(B, A - prices[i]), max(C, B + prices[i]), max(D, C - prices[i]), max(E, D + prices[i])
                
        return max(A, C, E)
'''
