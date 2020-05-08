# --------------------------------------------------------------------------
# Name:        Single Number
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty array of integers, every element appears twice except 
    for one. Find that single one.
    
    Example 1:
        Input: [2,2,1]
        Output: 1
    
    Example 2:
        Input: [4,1,2,1,2]
        Output: 4
    
    Note: Your algorithm should have a linear runtime complexity. 
          Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) == 1:
                return i
                


"""other faster methods (from other submissions)
##################################################
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
"""
