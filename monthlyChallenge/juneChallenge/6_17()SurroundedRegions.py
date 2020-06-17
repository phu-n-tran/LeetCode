# --------------------------------------------------------------------------
# Name:        Surrounded Regions
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a 2D board containing 'X' and 'O' (the letter O), capture all 
    regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    Example:
          X X X X
          X O O X
          X X O X
          X O X X
      
      After running your function, the board should be:
          X X X X
          X X X X
          X X X X
          X O X X
          
    Explanation:
        Surrounded regions shouldn’t be on the border, which means that 
        any 'O' on the border of the board are not flipped to 'X'. Any 'O'
        that is not on the border and it is not connected to an 'O' on the
        border will be flipped to 'X'. Two cells are connected if they are
        adjacent cells connected horizontally or vertically.
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        def fill(board, row, col):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
                board[row][col] = 'N'
                fill(board, row+1, col)
                fill(board, row, col+1)
                fill(board, row-1, col)
                fill(board, row, col-1)
        
        if board: 
            # filter any 'O' that touch the border
            for row in range(len(board)):
                fill(board, row, 0)
                fill(board, row, len(board[0])-1)

            for col in range(len(board[0])):
                fill(board, 0, col)
                fill(board, len(board)-1, col)

            # after filter, replace 'O' with 'X' and 'N' with 'O'
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == 'O':
                        board[row][col] = 'X'
                    elif board[row][col] == 'N':
                        board[row][col] = 'O'

    
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        M, N = len(board), len(board[0])
        
        # O -> G, Os connected with boundaries
        def dfs(r, c):
            if not(0 <= r < M and 0 <= c < N) or board[r][c] != 'O':
                return
            board[r][c] = 'G'
            for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(r + dr, c + dc)
        
        for i in xrange(M): 
            dfs(i, 0)
            dfs(i, N - 1)
        
        for j in xrange(N):
            dfs(0, j)
            dfs(M - 1, j)
        
        for i in xrange(M):
            for j in xrange(N):
                board[i][j] = 'O' if board[i][j] == 'G' else 'X'

'''
