# --------------------------------------------------------------------------
# Name:        Contains Duplicate III
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of integers, find out whether there are two distinct 
    indices i and j in the array such that the absolute difference between
    nums[i] and nums[j] is at most t and the absolute difference 
    between i and j is at most k.

    Example 1:
      Input: nums = [1,2,3,1], k = 3, t = 0
      Output: true
    
    Example 2:
      Input: nums = [1,0,1,1], k = 1, t = 2
      Output: true
    
    Example 3:
      Input: nums = [1,5,9,1,5,9], k = 2, t = 3
      Output: false
    
    Hints:
      1. Time complexity O(n logk) - This will give an indication that 
         sorting is involved for k elements.
      2. Use already existing state to evaluate next state - Like, a 
         set of k sorted numbers are only needed to be tracked. When we 
         are processing the next number in array, then we can utilize 
         the existing sorted state and it is not necessary to sort next
         overlapping set of k numbers again.
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # this line is importance, without this, the solution is TLE
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)):
            for j in range(i+1,  min(i+k+1, len(nums))):
                # print(i, j, abs(nums[i] - nums[j]))
                if abs(nums[i] - nums[j]) <= t:
                    return True
                
        return False

#         if t == 0 and len(nums) == len(set(nums)):
#             return False
        
#         for i, num in enumerate(nums):
#             for j in range(i+1, min(i+k+1, len(nums))):
#                 if abs(num - nums[j]) <= t:
#                     return True
                    
#         return False
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t == 0 and len(nums) == len(set(nums)):
            return False
        dic = {}

        for i in range(len(nums)):
            for key in dic.keys():
                if abs(key - nums[i]) <= t and abs(dic[key] - i) <= k:
                    return True
            dic[nums[i]] = i
        return False
##################################################
def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0: return False
        
        dic = {}
        for i in range(len(nums)):
            w = nums[i]/(t+1)
            
            if w in dic: return True
            if w-1 in dic and abs(nums[i]-dic[w-1]) <= t: return True
            if w+1 in dic and abs(nums[i]-dic[w+1]) <= t: return True
            dic[w] = nums[i]
            
            if i >= k: del dic[nums[i-k]/(t+1)]
                
        return False
##################################################
def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k<=0 or t<0:
            return False
        w = t+1
        buckets = {}
        for i,n in enumerate(nums):
            key = n/w
            if key in buckets:
                return True
            elif key-1 in buckets and n - buckets[key-1] < w:
                return True
            elif key+1 in buckets and buckets[key+1] - n < w:
                return True
            if i >= k :
                buckets.pop(nums[i-k]/w)
            buckets[key] = n
        return False
##################################################

'''
