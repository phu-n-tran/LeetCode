# --------------------------------------------------------------------------
# Name:        Unique Paths III
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    On a 2-dimensional grid, there are 4 types of squares:
      1. 1 represents the starting square.  There is exactly one starting square.
      2. 2 represents the ending square.  There is exactly one ending square.
      3. 0 represents empty squares we can walk over.
      4. -1 represents obstacles that we cannot walk over.
      5. Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


    Example 1:
      Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
      Output: 2
      Explanation: We have the following two paths: 
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
        2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

    Example 2:
      Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
      Output: 4
      Explanation: We have the following four paths: 
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
        2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
        3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
        4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
   
    Example 3:
      Input: [[0,1],[2,0]]
      Output: 0
      Explanation: 
        There is no path that walks over every empty square exactly once.
        Note that the starting and ending square can be anywhere in the grid.

    Note:
      1. 1 <= grid.length * grid[0].length <= 20
"""


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.ans, empty = 0, 0
        m, n = len(grid[0]), len(grid)
        def dfs(x, y, rest):
            if x < 0 or x >= n or y < 0 or y >= m or  grid[x][y] < 0: return
            if grid[x][y] == 2 and rest == 0:
                self.ans += 1
            
            neibs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in neibs:
                save = grid[x][y]
                grid[x][y] = -2
                dfs(x+dx, y+dy, rest - 1)
                grid[x][y] = save
            
        for i,j in product(range(n), range(m)):
            if grid[i][j] == 1: (sx, sy) = (i,j)
            empty += (grid[i][j] != -1)

        dfs(sx, sy, empty-1)
        return self.ans
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        start_cell, end_cell = None, None
        empty_cells = {} # the set of neighbors' positions for each cell

        # collect empty cells
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in [0, 1]:
                    empty_cells[(i, j)] = set()
                    if grid[i][j] == 1: start_cell = (i, j)
                elif grid[i][j] == 2: end_cell = (i, j)

        # collect their neighbors
        for x, y in empty_cells:
            for xch, ych in directions:
                neighbor = (x + xch, y + ych)
                if neighbor in empty_cells: empty_cells[(x, y)].add(neighbor)

        next_to_finish = set((end_cell[0] + xch, end_cell[1] + ych) for xch, ych in directions)
        visited=set([start_cell])
        def count_routes(cell=start_cell):
            left_to_visit = len(empty_cells) - len(visited)
            if not left_to_visit: return int(cell in next_to_finish)
            routes_to_end = 0
            for neighbor in (empty_cells[cell] - visited):
                visited.add(neighbor)
                routes_to_end += count_routes(neighbor)
                visited.remove(neighbor)
            return routes_to_end

        return count_routes()
##################################################
def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        A = grid
        self.res = 0
        m, n, empty = len(A), len(A[0]), 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if A[x][y] == 2:
                self.res += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0
        dfs(x, y, empty)
        return self.res
##################################################
def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.cnt = 0
        r, c, left = len(grid), len(grid[0]), 1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    left += 1
        def dfs(i, j, left):
            if not (0 <= i < r): return
            if not (0 <= j < c): return
            if grid[i][j] < 0: return
            if grid[i][j] == 2: 
                if left == 0:
                    self.cnt += 1
                return
            grid[i][j] = -2
            dfs(i-1, j, left-1)
            dfs(i+1, j, left-1)
            dfs(i, j-1, left-1)
            dfs(i, j+1, left-1)
            grid[i][j] = 0
            return
        dfs(x, y, left)            
        return self.cnt
##################################################
'''
