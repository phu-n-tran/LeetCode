# --------------------------------------------------------------------------
# Name:        Uncrossed Lines
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    We write the integers of A and B (in the order they are given) on two
    separate horizontal lines.

    Now, we may draw connecting lines: a straight line connecting two numbers
    A[i] and B[j] such that:

    A[i] == B[j];
    The line we draw does not intersect any other connecting (non-horizontal) line.
    Note that a connecting lines cannot intersect even at the endpoints: each
    number can only belong to one connecting line.

    Return the maximum number of connecting lines we can draw in this way.
    
    Example 1:
        Input: A = [1,4,2], B = [1,2,4]
        Output: 2
        Explanation: We can draw 2 uncrossed lines as in the diagram.
            We cannot draw 3 uncrossed lines, because the line from 
            A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
 
    Example 2:
        Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
        Output: 3
   
    Example 3:
        Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
        Output: 2
    
    Note: 
        1. 1 <= A.length <= 500
        2. 1 <= B.length <= 500
        3. 1 <= A[i], B[i] <= 2000
        
    Hint:
        Think dynamic programming. Given an oracle dp(i,j) that tells us 
        how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...]
        are uncrossed, can we write this as a recursion?
"""

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        m = len(B)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
        
        return dp[-1][-1]
        
        
          
            
        
 



        
"""other faster methods (from other submissions)
##################################################
def maxUncrossedLines(self, A, B):
        #A: List[int], B: List[int], return int
        
        if len(A) > len(B): #swap A, B if len(A) is longer
            A, B = B, A         
        n, m, h = len(A), len(B), collections.defaultdict(list)
        for i, num in enumerate(B): h[num].append(i)
        dp = [[-1]*m for _ in range(n)]
            
        def dfs(i, j):
            max_, i2 = 0, i+1
            list_ = h[A[i]] #list of possible indexes for a num in B
            if list_: #dfs when there is connection from A[i] to B
                bIndex = bisect.bisect_left(list_,j) #find next num in B to connect
                if bIndex < len(list_):
                    max_, bIndex,  = 1, list_[bIndex] #the real index in B
                    if bIndex >= j:
                        bIndex2 = bIndex+1
                        if i2 < n and bIndex2 < m:
                            if dp[i2][bIndex2] == -1:
                                dfs(i2, bIndex2)
                            max_ = max(max_, 1+dp[i2][bIndex2])
            if i2 < n: #dfs when there isn't connection from A[i] to B
                if dp[i2][j] == -1:
                    dfs(i2, j)
                max_ = max(max_, dp[i2][j])
                
            dp[i][j] = max_
            return max_
        
        return dfs(0,0)
"""
