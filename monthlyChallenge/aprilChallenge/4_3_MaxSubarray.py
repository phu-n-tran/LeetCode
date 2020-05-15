# --------------------------------------------------------------------------
# Name:        Maximum Subarray (Kadane's algorithm)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an integer array nums, find the contiguous subarray 
    (containing at least one number) which has the largest sum and return
    its sum.
    
    Example 1:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
    
    Follow Up:
    If you have figured out the O(n) solution, try coding another 
    solution using the divide and conquer approach, which is more subtle.
    
    Hint after approach:
    there will not be a larger sum that contain part of the current large sum
    ex: give [a, b, c, d, e, f, g, h], if bcd has the current largest sum
    then there will not be any and subarray that contain b,c, or d will contain
    a larger sum than current bcd (cdef or de) < bcd
    
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
            if greatest < current:
                greatest = current
                
            if current < 0:
                current = 0
        
        return greatest
                


"""other faster methods (from other submissions)
##################################################
def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                nums[i + 1] += nums[i]
        return max(nums)
##################################################
def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) < 2):
            return nums[0]
        
        check_sum = nums[0]
        
        start_index = 0
        end_index = 0
        sum_ = nums[0]
        for i in range(1, len(nums)):
            sum_ += nums[i]
            if(sum_ > nums[i]):
                if(sum_ > check_sum):
                    check_sum = sum_
                end_index = i
            else:
                start_index = i
                end_index = i
                sum_ = nums[i]
                if(nums[i] > check_sum):
                    check_sum = nums[i]
        return check_sum
#########################################
# 
def maxSubArraySum(a,size): 
      
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 

"""
