# --------------------------------------------------------------------------
# Name:        Dungeon Game
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    The demons had captured the princess (P) and imprisoned her in the
    bottom-right corner of a dungeon. The dungeon consists of M x N rooms
    laid out in a 2D grid. Our valiant knight (K) was initially positioned
    in the top-left room and must fight his way through the dungeon to 
    rescue the princess.

    The knight has an initial health point represented by a positive integer.
    If at any point his health point drops to 0 or below, he dies immediately.

    Some of the rooms are guarded by demons, so the knight loses health 
    (negative integers) upon entering these rooms; other rooms are either 
    empty (0's) or contain magic orbs that increase the knight's health 
    (positive integers).

    In order to reach the princess as quickly as possible, the knight 
    decides to move only rightward or downward in each step.

    Write a function to determine the knight's minimum initial health 
    so that he is able to rescue the princess.

    For example, given the dungeon below, the initial health of the knight
    must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

    -2(K)  -3	  3
    -5  	-10	  1
    10	   30	 -5(P)


    Note:
        1. The knight's health has no upper bound.
        2. Any room can contain threats or power-ups, even the first 
           room the knight enters and the bottom-right room where the 
           princess is imprisoned.
"""

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]
        
    
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        
        # instead of going from top left to bottom right start from bottom right then go upto top left 
        if not dungeon or not dungeon[0]: return 0
        # in n ** 2 space 
        rows, cols = len(dungeon), len(dungeon[0])
        
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                # if its the starting and the number is negative
                if row == rows - 1 and col == cols - 1:
                    if dungeon[row][col] < 0: dungeon[row][col] = abs(dungeon[row][col]) + 1
                    else: dungeon[row][col] = 1
                
                else:
                    if row == rows - 1: temp = dungeon[row][col + 1] - dungeon[row][col] # substracting from prev coz we moving right to left 
                    elif col == cols - 1 : temp = dungeon[row + 1][col] - dungeon[row][col] #moving up so add from the rows below for lst col
                    else: temp = min(dungeon[row][col + 1], dungeon[row + 1][col]) - dungeon[row][col] # min of prev and down ones - current
                    
                    if temp <= 0: dungeon[row][col] = 1 # reset to 1
                    else: dungeon[row][col] = temp
        return dungeon[0][0] """
    
        max_value = sys.maxsize/2

        rows, cols = len(dungeon), len(dungeon[0])

        dp = [max_value]*(cols+1)
        dp[cols-1] = 1


        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                dp[col] = max(1, min(dp[col], dp[col + 1]) - dungeon[row][col])
                
        return dp[0]
    
        # both these solutions run similarly
######################################
def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0

        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]

        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        
        return dp[0][0]
'''
