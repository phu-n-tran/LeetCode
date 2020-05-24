# --------------------------------------------------------------------------
# Name:        Interval List Intersections
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two lists of closed intervals, each list of intervals is pairwise 
    disjoint and in sorted order.

    Return the intersection of these two interval lists.

    (Formally, a closed interval [a, b] (with a <= b) denotes the set of real
    numbers x with a <= x <= b.  The intersection of two closed intervals is
    a set of real numbers that is either empty, or can be represented as a 
    closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
    
    Example 1:
        Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
    
    Note: 
        1. 0 <= A.length < 1000
        2. 0 <= B.length < 1000
        3. 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        iterA = 0
        iterB = 0
        result = []
        
        while iterA < len(A) and iterB < len(B):
            # print(iterA)
            # print(iterB)
            A0 = A[iterA][0]
            A1 = A[iterA][1]
            B0 = B[iterB][0]
            B1 = B[iterB][1]
            # case 1: when A is inside B (A=[2,3], B=[1,5])
            if B0 <= A0 and A1 <= B1:
                # print("case1")
                result.append(A[iterA])
                iterA += 1
            # case 2: when B is inside A (A=[1,4], B=[2,3])
            elif A0 <= B0 and B1 <= A1:
                # print("case2")
                result.append(B[iterB])
                iterB += 1
            # case 3: when 2nd half of A touch 1st half of B (A=[1,4], B=[3,6])
            elif A0 <= B0 < A1 and A1 <= B1:
                # print("case3")
                result.append([B0, A1])
                iterA += 1
            # case 4: when 1st half of A touch 2nd half of B (A=[3,6], B=[1,4])
            elif B0 <= A0 < B1 and B1 <= A1:
                # print("case4")
                result.append([A0, B1])
                iterB += 1
            # case 5: edge of A(end) and B(begin) touch
            elif A1 == B0:
                # print("case5")
                result.append([A1, A1])
                iterA += 1
            # case 6: edge of A(begin) and B(end) touch
            elif A0 == B1:
                # print("case6")
                result.append([A0, A0])
                iterB += 1
            # case 7: A does not intersect with B (A < B)
            elif A1 < B0:
                iterA += 1
            else:
                iterB += 1
            # print(result)
            # print("-----")
        return result
            
            
        
    










        
"""other faster methods (from other submissions)
##################################################
def intervalIntersection(self, a, b):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # if no overlap: increment the index of the lesser interval
        # if overlap: overlap interval = bigger start index + lower end index.
        # increment the index of the lesser interval
        i,j, res = 0, 0, []
        while i < len(a) and j < len(b):
            if a[i][1] < b[j][0]:
                i += 1
            elif b[j][1] < a[i][0]:
                j += 1
            else:
                res.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])]) 
                if a[i][1] > b[j][1]:
                    j += 1
                else:
                    i += 1
        return res
"""
