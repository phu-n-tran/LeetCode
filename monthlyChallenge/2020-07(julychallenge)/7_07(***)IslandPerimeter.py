# --------------------------------------------------------------------------
# Name:        Island Perimeter
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given a map in form of a two-dimensional integer grid where 1 
    represents land and 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The 
    grid is completely surrounded by water, and there is exactly one island
    (i.e., one or more connected land cells).

    The island doesn't have "lakes" (water inside that isn't connected to 
    the water around the island). One cell is a square with side length 1. 
    The grid is rectangular, width and height don't exceed 100. Determine 
    the perimeter of the island.

 

    Example:
      Input:
          [[0,1,0,0],
           [1,1,1,0],
           [0,1,0,0],
           [1,1,0,0]]
      Output: 16
      Explanation: 
        The perimeter is the 16 yellow stripes in the image below:
        SEE 7_07_example.PNG
        https://www.youtube.com/watch?time_continue=2&v=1Uw_y9H4z5E&feature=emb_logo
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row , col , count = len(grid) , len(grid[0]) , 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    count += 4
                    if x > 0 and grid[x - 1][y] == 1:
                        count -= 2
                    if y > 0 and grid[x][y - 1] == 1:
                        count -= 2
        return count
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        
        return result
##################################################
def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalCells = 0
        adjacentCells = 0
        prevIsCell = False
        
        for cell in grid[0]:
            if cell == 1:
                totalCells += 1
                if(prevIsCell):
                    adjacentCells += 1
                prevIsCell = True
            else:
                prevIsCell = False
                
        prevIsCell = False
        #we already covered grid[0]
        temp = grid[0]
        #skip first row
        if len(grid) > 1:
            for row in grid[1:]:
                index = 0;
                for cell in row:
                    if cell == 1:
                        totalCells += 1
                        if temp[index] == 1:
                            adjacentCells += 1
                        if(prevIsCell):
                            adjacentCells +=1
                        prevIsCell = True
                    else:
                        prevIsCell = False
                    index += 1
                temp = row
                prevIsCell = False
        return totalCells*4 - adjacentCells*2
##################################################
def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
        return perimeter
'''
