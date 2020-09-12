# --------------------------------------------------------------------------
# Name:        Maximum Product Subarray
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an integer array nums, find the contiguous subarray within an
    array (containing at least one number) which has the largest product.

    Example 1:
      Input: [2,3,-2,4]
      Output: 6
      Explanation: [2,3] has the largest product 6.

    Example 2:
      Input: [-2,0,-1]
      Output: 0
      Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = nums[::-1]
        
        for x in range(1,len(nums)):
            if nums[x - 1] != 0:
                nums[x] *= nums[x - 1]
                
            if B[x - 1] != 0:
                B[x] *= B[x - 1]
                
        return max(nums + B)
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reverse = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        
        # print nums,reverse
        
        return max(nums+reverse)
##################################################
 def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)
##################################################
def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        product = 1
        max_product = 0
        for i in range(0,len(nums)):
            product*=nums[i]
            max_product = max(max_product,product)
            if nums[i]==0:
                product = 1  
            
        print(max_product)
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product*=nums[i]
            max_product = max(max_product,product)  
            if nums[i]==0:
                product = 1
               
              
        print(max_product)
        return max_product
##################################################
'''
