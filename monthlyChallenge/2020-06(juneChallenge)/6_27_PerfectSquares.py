# --------------------------------------------------------------------------
# Name:        Perfect Squares
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a positive integer n, find the least number of perfect square 
    numbers (for example, 1, 4, 9, 16, ...) which sum to n.

    Example 1:
      Input: n = 12
      Output: 3 
      Explanation: 12 = 4 + 4 + 4.
      
    Example 2:
      Input: n = 13
      Output: 2
      Explanation: 13 = 4 + 9.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, dp):
            if dp[n] != -1:
                return dp[n]
            if n == 0:
                return 0
            
            minNum = float('inf')
            for i in range(1, int(sqrt(n))+1):
                cur = 1 + helper(n - i*i, dp)
                minNum = min(minNum, cur)
            dp[n] = minNum
            return minNum
                
        dp = [-1 for _ in range(n+1)]
        
        return helper(n, dp)
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4
        if int(math.sqrt(n))**2 == n:
            return 1
        i = 0
        while i ** 2 < n:
            j = math.sqrt(n - i**2)
            if int(j) == j:
                return 2
            i += 1
        return 3
##################################################
def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # i, dp = 1, [0] + [float('inf')] * (n)
        # for i in xrange(1, n+1):
        #     for j in range(1, int(math.sqrt(i))+1):
        #         dp[i] = min(dp[i], 1 + dp[i-int(j*j)])
        # return dp[-1]
        
        while not (n%4):       #results are the same for n and 4n
            n /= 4
        if n%8 == 7:
            return 4
        x = int(math.sqrt(n)+1)
        for i in range(x):
            j = math.floor(math.sqrt(n - i*i))
            if i*i + j*j == n:
                if i > 0 and j > 0:
                    return 2
                else:
                    return 1           
        return 3  
'''
