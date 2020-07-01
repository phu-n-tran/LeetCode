# --------------------------------------------------------------------------
# Name:        Single Element in an Sorted Array
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given a sorted array consisting of only integers where every 
    element appears exactly twice, except for one element which appears 
    exactly once. Find this single element that appears only once.
    
    Example 1:
        Input: [1,1,2,3,3,4,4,8,8]
        Output: 2
    
    Example 2:
        Input: [3,3,7,7,10,11,11]
        Output: 10
    
    Note: Your solution should run in O(log n) time and O(1) space.
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## too slow
        for i in set(nums):
            if nums.count(i) == 1:
                return i
        
        
        
        
        
        


"""other faster methods (from other submissions)
##################################################
def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == nums[mid-1]:
                if (mid - i) % 2 == 0:
                    j = mid - 2
                else:
                    i = mid + 1
            else:
                if (mid - i) % 2 == 1:
                    j = mid - 1
                else:
                    i = mid
        return nums[i]
#################################################
def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        
        return result
"""
 
