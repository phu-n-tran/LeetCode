# --------------------------------------------------------------------------
# Name:        Unique Paths
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    A robot is located at the top-left corner of a m x n grid 
    (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid 
    (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
    (see 6_29_illustration.png)
    Above is a 7 x 3 grid. How many possible unique paths are there?

    Example 1:
      Input: m = 3, n = 2
      Output: 3
      Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Right -> Down
        2. Right -> Down -> Right
        3. Down -> Right -> Right
    
    Example 2:
      Input: m = 7, n = 3
      Output: 28

    Constraints:
      1. 1 <= m, n <= 100
      2. It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # each block represent the current coordinate and its value represent the number of ways to move from origin to the current coordinate
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]    
            
        return dp[-1][-1]
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def binom(n, k):
    """n choose k, i.e. n! / (k! (n-k)!)"""
    result = 1
    for i in range(k+1, n+1):
        result *= i
    for i in range(1, n-k+1):
        result /= i
    return result

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return binom((m-1)+(n-1), n-1)
##################################################

'''
