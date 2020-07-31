# --------------------------------------------------------------------------
# Name:        Climbing Stairs
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
      Input: 2
      Output: 2
      Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
    
    Example 2:
      Input: 3
      Output: 3
      Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

    Constraints:
      1. 1 <= n <= 45
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # F[n] = F[n-1] + F[n-2]
        dp = (1, 1)
        for i in range(n-1):
            dp = (dp[1], dp[0] + dp[1])
        return dp[1]
    
    
        ###### Time Limit Exceeded
#         def DFS(n, curNumSteps, result):
#             if curNumSteps == n:
#                 result[0] += 1
#                 return
            
#             if curNumSteps > n:
#                 return
            
#             DFS(n, curNumSteps+1, result)
#             DFS(n, curNumSteps+2, result)
        
#         result = [0]
#         DFS(n, 0, result)
        
#         return result[0]
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
##################################################
def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range(2, n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]
##################################################
def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0] * (n + 1)
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]
##################################################
##################################################
'''
