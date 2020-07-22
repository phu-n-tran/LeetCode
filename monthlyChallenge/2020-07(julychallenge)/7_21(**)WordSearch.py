# --------------------------------------------------------------------------
# Name:        Word Search
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

    Example:
      board =
      [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
      ]

      Given word = "ABCCED", return true.
      Given word = "SEE", return true.
      Given word = "ABCB", return false.

    Constraints:
      1. board and word consists only of lowercase and uppercase English letters.
      2. 1 <= board.length <= 200
      3. 1 <= board[i].length <= 200
      4. 1 <= word.length <= 10^3
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        def dfs(index, i, j, count):
            if i<0 or i>= row or j<0 or j>=col or board[i][j]!=word[index]:
                return
            count += 1
            char = board[i][j]
            board[i][j] = 0
            if count == len(word):
                return True
            if dfs(index+1, i+1, j, count):
                return True
            if dfs(index+1, i-1, j, count):
                return True
            if dfs(index+1, i, j+1, count):
                return True
            if dfs(index+1, i, j-1, count):
                return True
            board[i][j] = char
            return False
        
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]: #search
                    if dfs(0, i, j, 0):
                        return True
        return False
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def preCheck():
            preDict = {}

            for i in word:
                if i in preDict: preDict[i]+=1
                else: preDict[i] = 1

            for i in board:
                for j in i:
                    if j in preDict and preDict[j]>0: preDict[j]-=1
            for i in preDict.values():
                if i>0: return False
            return True

        def helper(wordIdx, x, y):
            if board[x][y] != word[wordIdx]: return False
            elif wordIdx == l-1: return True
            else:
                wordIdx += 1
                tempChar = board[x][y]
                board[x][y] = None
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    xNext = x+d[0]
                    yNext = y+d[1]
                    if -1<xNext<m and -1<yNext<n and board[xNext][yNext]: 
                        if helper(wordIdx, xNext, yNext): return True
                board[x][y] = tempChar
                return False

        if not board: return False
        if not word: return True

        if not preCheck(): return False

        m = len(board)
        n = len(board[0])
        l = len(word)
        for i in xrange(m):
            for j in xrange(n):
                if helper(0,i,j): return True

        return False
##################################################
def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        visited = []
        for i in range(m):
            visited.append([0] * n)

        def foo(i, j, k):
            if k == len(word) - 1:
                return board[i][j] == word[k]
            if word[k] != board[i][j]:
                return False
            visited[i][j] = 1
            a, b, c, d = False, False, False, False
            if i + 1 < m:
                if visited[i+1][j] == 0:
                    a = foo(i+1, j, k+1)
            if j + 1 < n:
                if visited[i][j+1] == 0:
                    b = foo(i, j+1, k+1)
            if i - 1 >= 0:
                if visited[i-1][j] == 0:
                    c = foo(i-1, j, k+1)
            if j - 1 >= 0:
                if visited[i][j-1] == 0:
                    d = foo(i, j-1, k+1)
            if a or b or c or d:
                return True
            else:
                visited[i][j] = 0
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if foo(i, j, 0):
                        return True

        return False
##################################################
'''
