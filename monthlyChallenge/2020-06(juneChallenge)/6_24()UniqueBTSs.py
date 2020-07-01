# --------------------------------------------------------------------------
# Name:        Unique Binary Search Trees
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given n, how many structurally unique BST's (binary search trees) 
    that store values 1 ... n?

    Example:
        Input: 3
        Output: 5
        Explanation:
          Given n = 3, there are a total of 5 unique BST's:

                 1         3     3      2      1
                  \       /     /      / \      \
                   3     2     1      1   3      2
                  /     /       \                 \
                 2     1         2                 3
                 
    Explanation from:
        Count Number of Binary Search Tree Possible given n keys Dynamic Programming
            https://www.youtube.com/watch?v=YDf982Lb84o
    
    Approach:
      we know n=0 -> 1, n=1 -> 1, n=2 -> 2, n=3 -> 5
      as for n=4, we have 1,2,3,4
        for 1, we have n=0->1 * n=3->5 which is 5 ways
                1
                 \
                 {2,3,4}
             
        for 2, we have n=1->1 * n=2->2 which is 2
                2
              /   \
            {1}  {3,4}
        
        for 3, we have n=2->2 * n1->1 which is 2
               3
             /   \
          {1,2}  {4}
        for 4, we have n=3->5 * n0->1 which is 5
               4
             /
         {1,2,3}
        Hence, we will have n4 equal to (1*5)+(1*2)+(2*1)+(5*1) = 5+2+2+5 = 14 possible ways
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(i, dp):
            # break the problem down as the explanation in the approach section
            count = 0
            for k in range(1,i+1):
                count += dp[k-1] * dp[i-k]
            dp[i] = count
            
        # assume we know n=0 and n=1 both have 1 possible way
        dp = [1 for _ in range(n+1)]
        
        # calculate/accummulate value for each step of n
        for i in range(2, n+1):
            helper(i, dp)

        return dp[-1]
        
        
        
        
        
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1, 1, 2]
        if n >= 3:
            for i in range(3, n+1):
                val = 0 
                for j in range(i):
                    val += arr[j] * arr[i-j-1]
                arr.append(val)
            return arr[-1]
        else:
            return arr[n]
##################### same as below ############################
def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
#################################################
'''
