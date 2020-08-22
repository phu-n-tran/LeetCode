# --------------------------------------------------------------------------
# Name:        Sort Array By Parity
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array A of non-negative integers, return an array consisting
    of all the even elements of A, followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.

    Example 1:
      Input: [3,1,2,4]
      Output: [2,4,3,1]
      The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    Note:
      1. 1 <= A.length <= 5000
      2. 0 <= A[i] <= 5000
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddList = []
        evenList = []
        
        for num in A:
            if num % 2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
            
        return evenList + oddList
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other methods (from other submissions)
##################################################
def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key=lambda x:x%2)
        return A
##################################################
def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i <= j:
            if A[i] % 2 == 0:
                if A[j] % 2 == 0:
                    j += 1
            else:
                if A[j] % 2 == 0:
                    A[i], A[j] = A[j], A[i]
                else:
                    i -= 1
            i += 1
            j -= 1
        return A
##################################################
def sortArrayByParity(self, A):
        e=[]
        o=[]
        for i in range(0,len(A)):
            if A[i]%2==0:
                e.append(A[i])
            else:
                o.append(A[i])
        e.extend(o)
        return 
##################################################
'''
