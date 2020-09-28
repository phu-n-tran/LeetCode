# --------------------------------------------------------------------------
# Name:        Majority Element II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

    Follow-up: Could you solve the problem in linear time and in O(1) space?

    Example 1:
    Input: nums = [3,2,3]
    Output: [3]
    
    Example 2:
    Input: nums = [1]
    Output: [1]
    
    Example 3:
    Input: nums = [1,2]
    Output: [1,2]

    Constraints:
      1. 1 <= nums.length <= 5 * 104
      2. -109 <= nums[i] <= 109
    
    Hint:
      1. How many majority elements could it possibly have? Do you have a better hint? Suggest it!
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maj = len(nums) // 3
        dic = {}
        
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        return [ele for ele in dic if dic[ele] > maj]
        
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other methods (from other submissions)
##################################################
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=collections.defaultdict(int)
        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        n=len(nums)
        l=[]
        for i in m:
            if m[i]>n/3:
                l.append(i)
        return l
##################################################
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        counts = {}
        
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
                
        threshold = len(nums)/3
        ans = []
        
        for i in counts:
            if counts[i] > threshold:
                ans.append(i)
        
        return ans
##################################################
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n=len(nums)
        ans=[]
        count=0
        pt=nums[0]
        for i in range(len(nums)):
            if pt==nums[i]:
                count+=1
            else:
                if count>(n/3):
                    ans.append(pt)
                pt=nums[i]
                count=1
        if count>n/3:
            ans.append(pt)
        return ans
##################################################
'''
