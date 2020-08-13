# --------------------------------------------------------------------------
# Name:        Pascal's Triangle II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

    Note that the row index starts from 0.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:
      Input: 3
      Output: [1,3,3,1]
    
    Follow up:
      Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result = [1]
        
        for i in range(1, rowIndex + 1):
            result.append(int(result[i - 1] * (rowIndex - (i - 1)) / i))
        
        return result
        
        ### TLE - Time Limit Exceeded
#        # to calculate this, we can use combination nCr where 
#        # n is the rowIndex, the row that we are on
#        # r is the index of the current position (column) that we want to find the value on a particular row
#         from itertools import combinations
#         n = "A" * rowIndex
#         result = []
#         for r in range(rowIndex+1):
#             result.append(len(list(combinations(n, r))))
        
#         return result
        
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [[], []]
        for i in range(rowIndex+1):
            for j in range(i+1):
                if j >= len(ans[i % 2]):
                    if j == 0 or j == i:
                        ans[i % 2].append(1)
                    else:
                        ans[i % 2].append(ans[(i+1) % 2][j-1] + ans[(i+1) % 2][j])
                else:
                    if j == 0 or j == i:
                        ans[i % 2][j] = 1
                    else:
                        ans[i % 2][j] = ans[(i+1) % 2][j-1] + ans[(i+1) % 2][j]
        return ans[i % 2]
##################################################
def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]*(rowIndex+1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                row[j] += row[j-1]
        return row
##################################################
def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        arr=[1]
        lr=self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            var=lr[i-1]+lr[i]
            arr.append(var)
        arr.append(1)
        return arr
'''
