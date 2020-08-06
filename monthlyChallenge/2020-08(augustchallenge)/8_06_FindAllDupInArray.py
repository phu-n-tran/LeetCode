# --------------------------------------------------------------------------
# Name:        Find All Duplicates in an Array
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some 
    elements appear twice and others appear once.

    Find all the elements that appear twice in this array.

    Could you do it without extra space and in O(n) runtime?

    Example:
      Input:
        [4,3,2,7,8,2,3,1]
      Output:
        [2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                result.append(nums[i])
        return result
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        ans = []
        for x in nums:
            if x in dict:
                ans.append(x)
            else:
                dict[x] = 0
        return ans
##################################################
def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums)
        for i in nums:
            nums[(i%n)-1]+=n
        res=[]
        for i, num in enumerate(nums):
            if num>2*n:
                res.append(i+1)
        return res
##################################################

'''
