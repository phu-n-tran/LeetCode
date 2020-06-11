# --------------------------------------------------------------------------
# Name:        Sort Colors
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array with n objects colored red, white or blue, sort them 
    in-place so that objects of the same color are adjacent, with the colors 
    in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color 
    red, white, and blue respectively.

    Note: You are not suppose to use the library's sort function for this problem.

    Example:
        Input: [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
          
    Follow up:
        1. A rather straight forward solution is a two-pass algorithm using 
           counting sort.
        2. First, iterate the array counting number of 0's, 1's, and 2's, 
           then overwrite array with total number of 0's, then 1's and followed by 2's.
        3. Could you come up with a one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if low != i or low != i+1:
                    nums.pop(i)
                    nums.insert(low, 0)
                low += 1
                mid += 1
                high += 1
            elif nums[i] == 1:
                if mid != i or mid != i+1:
                    nums.pop(i)
                    nums.insert(mid, 1)
                mid += 1
                high += 1
            else:
                if high != i or high != i+1:
                    nums.pop(i)
                    nums.insert(high, 2)
                high += 1
        
            
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,m,r = 0,0,len(nums)-1
        while m <= r:
            if nums[m] == 0:
                nums[l],nums[m] = nums[m],nums[l]
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m],nums[r] = nums[r],nums[m]
                r -= 1
        return nums
'''
