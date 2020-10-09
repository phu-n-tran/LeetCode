
# --------------------------------------------------------------------------
# Name:        K-diff Pairs in an Array
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of integers nums and an integer k, return the number of 
    unique k-diff pairs in the array.

    A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
      1. 0 <= i, j < nums.length
      2. i != j
      3. |nums[i] - nums[j]| == k
      4. Notice that |val| denotes the absolute value of val.


    Example 1:
      Input: nums = [3,1,4,1,5], k = 2
      Output: 2
      Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
        Although we have two 1s in the input, we should only return the number of unique pairs.
    
    Example 2:
      Input: nums = [1,2,3,4,5], k = 1
      Output: 4
      Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    
    Example 3:
      Input: nums = [1,3,1,5,4], k = 0
      Output: 1
      Explanation: There is one 0-diff pair in the array, (1, 1).

    Example 4:
      Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
      Output: 2
    
    Example 5:
      Input: nums = [-1,-2,-3], k = 1
      Output: 2

    Constraints:
      1. 1 <= nums.length <= 104
      2. -107 <= nums[i] <= 107
      3. 0 <= k <= 107
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0: # looking for pair of same number
            dictNums = {}
            for i in nums:
                dictNums[i] = dictNums.get(i, []) + [i]
            return sum(len(dictNums[key]) > 1 for key in dictNums)
        else: # looking for pair that add up to k
            setNums = set(nums)
            return sum(i+k in nums for i in setNums)
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = Counter(nums)
        res = 0
        for x in s.keys():
            t = x-k
            if t in s:
                if x != t:
                    res += 1
                else:
                    if s[t] > 1:
                        res += 1
        return res
##################################################
def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for n, c in count.items():
                if c > 1:
                    res += 1
            return res
        else:
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    res += 1
            return res
##################################################
def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        out = 0
        for num in nums:
            if k==0 and num in d and d[num]==1: 
                out+=1
                d[num]+=1
            if num not in d:
                if (k+num) in d: out+=1
                if (num-k) in d: out+=1
                d[num]=1
            
        return out
##################################################
'''
