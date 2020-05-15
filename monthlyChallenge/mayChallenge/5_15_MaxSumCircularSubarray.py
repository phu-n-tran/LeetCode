# --------------------------------------------------------------------------
# Name:        Maximum Sum Circular Subarray
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a circular array C of integers represented by A, find the maximum
    possible sum of a non-empty subarray of C.

    Here, a circular array means the end of the array connects to the 
    beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length,
    and C[i+A.length] = C[i] when i >= 0.)

    Also, a subarray may only include each element of the fixed buffer A at
    most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does
    not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
    
    Example 1:
        Input: [1,-2,3,-2]
        Output: 3
        Explanation: Subarray [3] has maximum sum 3
    
    Example 2:
        Input: [5,-3,5]
        Output: 10
        Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
    
    Example 3:
        Input: [3,-1,2,-1]
        Output: 4
        Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
    
    Example 4:
        Input: [3,-2,2,-3]
        Output: 3
        Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
        
    Example 5:
        Input: [-2,-3,-1]
        Output: -1
        Explanation: Subarray [-1] has maximum sum -1
        
    Note: 
        1. -30000 <= A[i] <= 30000
        2. 1 <= A.length <= 30000
"""

import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        greatest = -sys.maxint
        current = 0
        
        for i in range(len(nums)):
            current += nums[i]
            greatest = max(current, greatest)
            current = max(current, 0)
        
        return greatest
    
    def minSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = sys.maxint
        current = 0
        
        for i in range(len(nums)):
            current += nums[i]
            smallest = min(current, smallest)
            current = min(current, 0)
        
        return smallest
    
    
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # case 1
        result1 = self.maxSubArray(A)
        
        # case 2: total - min = max (w/ circular loop)
        total = sum(A)
        result2 = total - self.minSubArray(A)
        print(total)
        print(self.minSubArray(A))
        
        return result1 if result1<0 else max(result1, result2)
        







        
"""other faster methods (from other submissions)
##################################################
def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        t1=A[:]
        t2=A[:]
        c=0
        for i in range(1,len(A)):
            if t1[i-1]>0:     #find max one without circular
                t1[i]+=t1[i-1]
                c=1
            if t2[i-1]<0:     #find min one without circular
                t2[i]+=t2[i-1]
        if c==0:
            return max(A)
        return max(max(t1),(sum(A)-min(t2)))
"""
