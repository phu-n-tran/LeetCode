# --------------------------------------------------------------------------
# Name:        Subarray Product Less Than K
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Your are given an array of positive integers nums.

    Count and print the number of (contiguous) subarrays where the product
    of all the elements in the subarray is less than k.

    Example 1:
      Input: nums = [10, 5, 2, 6], k = 100
      Output: 8
      Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
      Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
    
    Note:
      1. 0 < nums.length <= 50000.
      2. 0 < nums[i] < 1000.
      3. 0 <= k < 10^6.
     
     Hint: For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        out, beg, end, P = 0, 0, 0, 1
        while end < len(nums):
            P *= nums[end]
            while end >= beg and P >= k:
                P /= nums[beg]
                beg += 1
            out += end - beg + 1
            end += 1
        return out
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        count = 0
        start = 0
        product = 1
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k:
                product = product // nums[start]
                start += 1
            count += end-start+1
        return count
##################################################
def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
##################################################

##################################################
'''
