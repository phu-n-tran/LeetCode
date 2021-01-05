# --------------------------------------------------------------------------
# Name:        Search a 2D Matrix
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Write an efficient algorithm that searches for a value in an m x n matrix. 
    This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.


    Example 1:
      Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
      Output: true
    
    Example 2:
      Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
      Output: false

    Constraints:
      1) m == matrix.length
      2) n == matrix[i].length
      3) 1 <= m, n <= 100
      4) -104 <= matrix[i][j], target <= 104
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        start = 0
        end = len(matrix) - 1
        selectedRow = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        while start <= end:
            mid = (start + end) // 2
            # print(start, end, mid)
            
            if matrix[mid][0] == target or matrix[mid][n-1] == target:
                return True
            
            if matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][0] < target and matrix[mid][n-1] > target:
                selectedRow = matrix[mid]
                break
            else: # matrix[mid][n] > target
                start = mid + 1
            # print("ooo", start, end, mid)

        
        return target in selectedRow
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def searchMatrix(self, matrix, target):
        def bisect_left(arr, num):   
            if not arr: return 0
            left, right = 0, len(arr) - 1
            while left < right:
                center = (left + right) // 2
                if num > arr[center]:
                    left = center + 1
                else:
                    right = center
            return left
        if not matrix: return False
        if not matrix[0]: return False
        
        string_index = bisect_left([line[-1] for line in matrix], target)
        if string_index < len(matrix):
            column_index = bisect_left(matrix[string_index], target)
            if column_index < len(matrix[string_index]):
                return matrix[string_index][column_index] == target
        return False
##################################################
def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False
##################################################
##################################################
'''
