# --------------------------------------------------------------------------
# Name:        Image Overlap
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Two images A and B are given, represented as binary, square matrices
    of the same size.  (A binary matrix has only 0s and 1s as values.)

    We translate one image however we choose (sliding it left, right, up, 
    or down any number of units), and place it on top of the other image.
    After, the overlap of this translation is the number of positions that
    have a 1 in both images.

    (Note also that a translation does not include any kind of rotation.)

    What is the largest possible overlap?

    Example 1:
      Input: A = [[1,1,0],
                  [0,1,0],
                  [0,1,0]]
             B = [[0,0,0],
                  [0,1,1],
                  [0,0,1]]
      Output: 3
      Explanation: We slide A to right by 1 unit and down by 1 unit.
    
    Notes: 
      1. 1 <= A.length = A[0].length = B.length = B[0].length <= 30
      2. 0 <= A[i][j], B[i][j] <= 1
    
    https://leetcode.com/problems/image-overlap/solution/
"""


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        import numpy as np
        import scipy.signal
        return scipy.signal.correlate2d(np.array(A), np.array(B)).max()
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        listA, listB = [], []
        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                if A[i][j]:
                    listA.append((i, j))
                if B[i][j]:
                    listB.append((i, j))
        difference = defaultdict(int)
        for ai, aj in listA:
            for bi, bj in listB:
                difference[ai - bi, aj - bj] += 1
        return max(difference.values()) if difference else 0
##################################################
def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        LA = [i / N * 100 + i % N for i in xrange(N * N) if A[i / N][i % N]]
        LB = [i / N * 100 + i % N for i in xrange(N * N) if B[i / N][i % N]]
        c = collections.Counter(i - j for i in LA for j in LB)
        return max(c.values() or [0])
##################################################
def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        def count_ones(n):
            res = 0
            while n > 0:
                res += 1
                n -= n&(-n)
            return res
        m,n = len(A), len(A[0])
        bin_a = []
        bin_b = []
        for i in range(m):
            temp_a = temp_b = 0
            for j in range(n):
                temp_a = (temp_a<<1) + A[i][j]
                temp_b = (temp_b<<1) + B[i][j]
            bin_a += [temp_a]
            bin_b += [temp_b<<n]
        bin_b = [0]*m+bin_b+[0]*m
        res = 0
        for i in range(2*m):
            for j in range(2*n):
                temp = 0
                for a,b in zip(bin_a, bin_b[i:i+m]):
                    temp += count_ones(a&(b>>j))
                res = max(res,temp)
        return res
##################################################
def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        L = len(A)
        max_sum = 0
        if L == 0:
            return 0
        for i in range(L):
            for j in range(L):
                sum = 0
                sum2 = 0
                for k in range (i, L):
                    for l in range(j, L):
                        sum += A[k - i][l - j] * B[k][l]
                        sum2 += B[k - i][l - j] * A[k][l]
                max_sum = max(max_sum, sum)
                max_sum = max(max_sum, sum2)
        return max_sum
##################################################
def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M, and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up and left is equivalent to
                moving the other matrix down and right
            """
            count = 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        count += 1
            return count

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps
'''
