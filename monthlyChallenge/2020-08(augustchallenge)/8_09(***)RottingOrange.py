# --------------------------------------------------------------------------
# Name:        Rotting Oranges
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

    Example 1:
      Input: [[2,1,1],[1,1,0],[0,1,1]]
      Output: 4
    
    Example 2:
      Input: [[2,1,1],[0,1,1],[1,0,1]]
      Output: -1
      Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    
    Example 3:
      Input: [[0,2]]
      Output: 0
      Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

    Note:
      1. 1 <= grid.length <= 10
      2. 1 <= grid[0].length <= 10
      3. grid[i][j] is only 0, 1, or 2.
"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        
        result = 0
        sources = self.getsources(grid, m, n)
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = collections.deque(sources)
        level = 0
        while q:
            size = len(q)
            if level > 0: result += 1
            level += 1
            for k in range(size):
                i, j = q.popleft()
                
                for d in directions:
                    newi = i + d[0]
                    newj = j + d[1]
                    if m > newi >= 0 and n > newj >= 0 and grid[newi][newj] == 1:
                        grid[newi][newj] = 2
                        q.append((newi, newj))
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
                
        return result
                    
            
    def getsources(self, grid, m, n):
        sources = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    sources.append((i, j))
                    
        return sources
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        print(queue)
        print(fresh_oranges)
        
        queue.append((-1, -1))

        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes_elapsed += 1
                if queue:  
                    queue.append((-1, -1))
            else:
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if rows > neighbor_row >= 0 and cols > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))

        return minutes_elapsed if fresh_oranges == 0 else -1
##################################################
def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        q = deque()
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    q.append((i, j))

        distance = -1 if q else 0
        
        while q:
                        
            for _ in xrange(len(q)):
                
                i, j = q.pop()
                
                if i > 0 and grid[i-1][j] == 1:
                    q.appendleft((i - 1, j))
                    grid[i-1][j] = 2
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    q.appendleft((i + 1, j))
                    grid[i+1][j] = 2
                if j > 0 and grid[i][j-1] == 1:
                    q.appendleft((i, j-1))
                    grid[i][j-1] = 2
                if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                    q.appendleft((i, j+1))
                    grid[i][j+1] = 2
                    
            distance += 1

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    return -1
        
        return distance
##################################################
def orangesRotting(self, grid):
        lx=len(grid)
        ly=len(grid[0])
        rotten=deque()
        mi=0
        for i in range(lx):
            for j in range(ly):
                if grid[i][j]==2:
                    rotten.append([i,j,0])
        while rotten:
            r,c,mi=rotten.popleft()
            if r+1<lx and grid[r+1][c]==1:
                grid[r+1][c]=2
                rotten.append([r+1,c,mi+1])
            if r-1>=0 and grid[r-1][c]==1:
                grid[r-1][c]=2
                rotten.append([r-1,c,mi+1])
            if c-1>=0 and grid[r][c-1]==1:
                grid[r][c-1]=2
                rotten.append([r,c-1,mi+1])
            if c+1<ly and grid[r][c+1]==1:
                grid[r][c+1]=2
                rotten.append([r,c+1,mi+1])
        if any(1 in row for row in grid):
    
            return -1
        return mi
'''
