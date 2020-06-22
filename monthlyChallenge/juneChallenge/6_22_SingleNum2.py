# --------------------------------------------------------------------------
# Name:        Single Number II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty array of integers, every element appears three times
    except for one, which appears exactly once. Find that single one.

    Note: 
        Your algorithm should have a linear runtime complexity. 
        Could you implement it without using extra memory?

    Example 1:
        Input: [2,2,3,2]
        Output: 3
    
    Example 2:
        Input: [0,1,0,1,0,1,99]
        Output: 99
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        i = 0
        
        while i < len(nums):
            # check if the next element is out of bound or the current number is a single
            if i+1 == len(nums) or nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 3

            
    
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        threes = 0
        
        for num in nums:            
            twos = twos | (ones & num)
            ones ^= num  
            threes = twos & ones            
            twos = twos & ~threes
            ones = ones & ~threes   
                        
        return ones
##################################################
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(set(nums))-sum(nums))//2
'''
