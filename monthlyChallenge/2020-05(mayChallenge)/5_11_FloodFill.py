# --------------------------------------------------------------------------
# Name:        Flood Fill
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    An image is represented by a 2-D array of integers, each integer 
    representing the pixel value of the image (from 0 to 65535).

    Given a coordinate (sr, sc) representing the starting pixel 
    (row and column) of the flood fill, and a pixel value newColor, 
    "flood fill" the image.

    To perform a "flood fill", consider the starting pixel, plus any pixels
    connected 4-directionally to the starting pixel of the same color as the 
    starting pixel, plus any pixels connected 4-directionally to those pixels
    (also with the same color as the starting pixel), and so on. Replace the 
    color of all of the aforementioned pixels with the newColor.

    At the end, return the modified image.
    
    Example 1:
        Input: 
            image = [[1,1,1],[1,1,0],[1,0,1]]
            sr = 1, sc = 1, newColor = 2
        Output: [[2,2,2],[2,2,0],[2,0,1]]
        Explanation: 
            From the center of the image (with position (sr, sc) = (1, 1)),
            all pixels connected by a path of the same color as the starting
            pixel are colored with the new color.
            Note the bottom corner is not colored 2, because it is not 
            4-directionally connected to the starting pixel.
     
    Note:
        1) The length of image and image[0] will be in the range [1, 50].
        2) The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
        3) The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor or len(image) == 0:
            return image
        
        oldColor = image[sr][sc]
        self.helper(image, sr, sc, newColor, oldColor)
        
        return image
    
    def helper(self, image, sr, sc, newColor, oldColor):
        if 0 > sr or 0 > sc or len(image) <= sr or len(image[0]) <= sc or oldColor != image[sr][sc]:
            return
       
        image[sr][sc] = newColor
        self.helper(image, sr+1, sc, newColor, oldColor)
        self.helper(image, sr-1, sc, newColor, oldColor)
        self.helper(image, sr, sc+1, newColor, oldColor)
        self.helper(image, sr, sc-1, newColor, oldColor)
        
        
        
        
        
"""other faster methods (from other submissions)
##################################################
def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
"""
