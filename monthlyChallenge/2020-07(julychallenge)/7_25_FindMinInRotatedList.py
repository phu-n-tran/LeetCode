# --------------------------------------------------------------------------
# Name:        Find Minimum in Rotated Sorted Array II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Suppose an array sorted in ascending order is rotated at some pivot 
    unknown to you beforehand.
    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.
    The array may contain duplicates.

    Example 1:
    Input: [1,3,5]
    Output: 1
    
    Example 2:
    Input: [2,2,2,0,1]
    Output: 0
    
    Note:
      1. This is a follow up problem to Find Minimum in Rotated Sorted Array.
      2. Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
        # return sorted(set(nums))[0]
        
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end-start)/2
            if nums[mid] > nums[end]:
                start = mid+1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
        return nums[start]
##################################################
def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return "0"
        min_val = nums[0]

        for i in range (1,len(nums)):
            if nums[i]<min_val:
                return nums[i]
        return min_val
##################################################
def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left=0
        right=len(nums)-1
        
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid
            else:
                right-=1
                
        #print(left, mid, right)
        return nums[left]
'''
