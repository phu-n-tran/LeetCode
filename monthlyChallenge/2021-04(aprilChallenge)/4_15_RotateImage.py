# --------------------------------------------------------------------------
# Name:        Rotate Image
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given an n x n 2D matrix representing an image, rotate the image 
    by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify 
    the input 2D matrix directly. DO NOT allocate another 2D matrix and do
    the rotation.
    

    Example 1:
      Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
      Output: [[7,4,1],[8,5,2],[9,6,3]]
    
    Example 2:
      Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
      Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
   
    Example 3:
      Input: matrix = [[1]]
      Output: [[1]]
   
    Example 4:
      Input: matrix = [[1,2],[3,4]]
      Output: [[3,1],[4,2]]


    Constraints:
      matrix.length == n
      matrix[i].length == n
      1 <= n <= 20
      -1000 <= matrix[i][j] <= 1000
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        
        for i in range(0, len(matrix)//2):
            margin = 0
            for k in range(i, col):
                temp = matrix[i][k] 
                matrix[i][k] = matrix[i+margin][col] # store origin value 
                matrix[i+margin][col] = temp   # ..update top-right 
                # print(i,k, temp,  matrix[i][k], matrix[i+margin][col])
                # print(row, col, matrix)
                
                temp = matrix[i][k]
                matrix[i][k] = matrix[row][col-margin]
                matrix[row][col-margin] = temp # ..update bottom-right
                # print(i,k, temp,  matrix[i][k], matrix[row][col-margin])
                # print(row, col, matrix)
                
                temp = matrix[i][k] 
                matrix[i][k] = matrix[row-margin][i]   # ..update top-left
                matrix[row-margin][i] = temp   # ..update bottom-left
                # print(i,k, temp,  matrix[i][k], matrix[row-margin][i])
                # print(row, col, matrix)
                margin = margin + 1
            
            row = row -1
            col = col -1
                
'''                
##################################################3
#other solution(s)#############################
# https://leetcode.com/problems/rotate-image/solution/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        
        for i in range(C):
            for j in range(i,C):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in range(R):
            matrix[row] = matrix[row][::-1]




'''
