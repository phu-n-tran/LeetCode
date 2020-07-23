# --------------------------------------------------------------------------
# Name:        Single Number III
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of numbers nums, in which exactly two elements appear 
    only once and all the other elements appear exactly twice. Find the 
    two elements that appear only once.

    Example:
      Input:  [1,2,1,3,2,5]
      Output: [3,5]
    
    Note:
      1. The order of the result is not important. 
         So in the above example, [5, 3] is also correct.
      2. Your algorithm should run in linear runtime complexity. 
         Could you implement it using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        for i in nums:
            if i in result:
                result.remove(i)
            else:
                result.append(i)
        return result
        
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic ={}
        for ele in nums:
            if ele not in dic:
                dic[ele]=1
            else:
                dic[ele]+=1
        for ele in dic:
            if dic[ele]==1:
                res.append(ele)
                
        return res
##################################################
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for num in nums:
            x ^= num
        diff = x & (-x)
        res = 0
        for num in nums:
            if diff & num:
                res ^= num
        return [res, x^res]
##################################################
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        res = []
        for num, c in count.items():
            if c == 1:
                res.append(num)
        return res
'''
