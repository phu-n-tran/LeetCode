# --------------------------------------------------------------------------
# Name:        Arranging Coins
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You have a total of n coins that you want to form in a staircase shape,
    where every k-th row must have exactly k coins.

    Given n, find the total number of full staircase rows that can be formed.

    n is a non-negative integer and fits within the range of a 32-bit signed integer.

    Example 1:
      n = 5
        The coins can form the following rows:
        ¤
        ¤ ¤
        ¤ ¤
        Because the 3rd row is incomplete, we return 2.
    
    Example 2:
      n = 8
        The coins can form the following rows:
        ¤
        ¤ ¤
        ¤ ¤ ¤
        ¤ ¤
        Because the 4th row is incomplete, we return 3.
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        while count < n:
            count += 1
            n -= count
        
        return count
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
#         if n < 2:
#             return n
#         dp = [0] * (n+1)
#         dp[0] = 0
#         dp[1] = 1
#         dp[2] = 1
        
#         k = 0
#         c = 2
        
#         for i in range(3, n+1):
#             if k != 0:
#                 dp[i] = dp[i-1]
#                 k -= 1
#             elif k == 0:
#                 dp[i] = dp[i-1] + 1
#                 k += 1
#                 k *= c
#                 c += 1
#         return dp[n]
        
        
        return (int)(((2*n + 0.25) ** 0.5) - 0.5)
#         k = 1
#         ans = 0
#         if n == 1:
#             return 1
#         elif n == 0:
#             return 0
#         while n > 0:
#             n -= k
#             k += 1
#             ans += 1
        
#         if n == 0:
#             return ans
#         return (ans - 1)
##################################################
def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Naive
        """count=0
        i = 1
        
        while n>=0:
            if n-i>=0: 
                n-=i
                i+=1
                count+=1
            else:
                break
        return count"""
        
        start = 1
        end = n
        
        while start<=end:
            
            mid=(start+end)//2
            k=(mid*(mid+1))//2
            
            if k==n:
                return mid
            if k<n:
                start=mid+1
            else:
                end = mid-1
                
        return end
##################################################
def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
'''
