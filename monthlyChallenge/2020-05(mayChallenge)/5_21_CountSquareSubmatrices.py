# --------------------------------------------------------------------------
# Name:        Count Square Submatrices with All Ones
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a m * n matrix of ones and zeros, return how many square 
    submatrices have all ones.
    
    Example 1:
        Input: matrix =
            [
              [0,1,1,1],
              [1,1,1,1],
              [0,1,1,1]
            ]
        Output: 15
        Explanation: 
            There are 10 squares of size 1.
            There are 4 squares of size 2.
            There is  1 square of size 3.
            Total number of squares = 10 + 4 + 1 = 15.
     
    Example 2:
        Input: matrix = 
            [
              [1,0,1],
              [1,1,0],
              [1,1,0]
            ]
        Output: 7
        Explanation: 
            There are 6 squares of size 1.  
            There is 1 square of size 2. 
            Total number of squares = 6 + 1 = 7.
    
    Constraints:
        1) 1 <= arr.length <= 300
        2) 1 <= arr[0].length <= 300
        3) 0 <= arr[i][j] <= 1
        
    Hints:
        1) Create an additive table that counts the sum of elements of 
           submatrix with the superior corner at (0,0).
        2) Loop over all subsquares in O(n^3) and check if the sum make 
           the whole array to be ones, if it checks then add 1 to the answer.
"""
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        result = 0
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        result += 1
                    else:
                        matrix[row][col] = min(matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1]) + 1
                        result += matrix[row][col]
        
        return result
                    
                
        
        



        
"""My other slower solution
"""
