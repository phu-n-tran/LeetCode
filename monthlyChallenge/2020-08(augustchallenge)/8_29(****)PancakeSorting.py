# --------------------------------------------------------------------------
# Name:        Pancake Sorting
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of integers A, We need to sort the array performing a 
    series of pancake flips.

    In one pancake flip we do the following steps:

    Choose an integer k where 0 <= k < A.length.
    Reverse the sub-array A[0...k].
    For example, if A = [3,2,1,4] and we performed a pancake flip 
    choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] 
    after the pancake flip at k = 2.

    Return an array of the k-values of the pancake flips that should be
    performed in order to sort A. Any valid answer that sorts the array 
    within 10 * A.length flips will be judged as correct.

    Example 1:
      Input: A = [3,2,4,1]
      Output: [4,2,4,3]
      Explanation: 
        We perform 4 pancake flips, with k values 4, 2, 4, and 3.
        Starting state: A = [3, 2, 4, 1]
        After 1st flip (k = 4): A = [1, 4, 2, 3]
        After 2nd flip (k = 2): A = [4, 1, 2, 3]
        After 3rd flip (k = 4): A = [3, 2, 1, 4]
        After 4th flip (k = 3): A = [1, 2, 3, 4], which is sorted.
        Notice that we return an array of the chosen k values of the pancake flips.

    Example 2:
      Input: A = [1,2,3]
      Output: []
      Explanation: The input is already sorted, so there is no need to flip anything.
        Note that other answers, such as [3, 3], would also be accepted.

    Constraints:
      1. 1 <= A.length <= 100
      2. 1 <= A[i] <= A.length
      3. All integers in A are unique (i.e. A is a permutation of the integers from 1 to A.length).
"""


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result, n = [], len(A)
        for i in range(n,0,-1):
            pl = A.index(i)
            if pl == i-1: continue
            if pl != 0:
                result.append(pl+1)
                A[:pl+1] = A[:pl+1][::-1]
            result.append(i)
            A[:i] = A[:i][::-1]
            
        return result
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        if not A or len(A)==1:
            return []
        
        n = len(A)
        res = []
        for num in range(n, 1, -1):
            idx = A.index(num)
            if idx == num-1:
                continue
            res.append(idx+1)
            A = A[idx::-1]+A[idx+1:]
            res.append(num)
            A = A[num-1::-1]+A[num:]
        
        return res
##################################################
def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res
##################################################
def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return []
        
        m = len(A)
        out = []
        
        while m > 0:
            if A[m-1] != m:
                idx = A.index(m)
                if idx != 0:
                    out.append(idx+1)
                    A = A[:idx+1][::-1] + A[idx+1:]
                out.append(m)
                A = A[:m][::-1]+A[m+1:]
            m -= 1
        return out
'''
