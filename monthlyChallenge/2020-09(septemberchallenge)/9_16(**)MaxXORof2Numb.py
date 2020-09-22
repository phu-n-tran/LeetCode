# --------------------------------------------------------------------------
# Name:        Maximum XOR of Two Numbers in an Array
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an integer array nums, return the maximum result of 
    nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

    Follow up: Could you do this in O(n) runtime?

    Example 1:
      Input: nums = [3,10,5,25,2,8]
      Output: 28
      Explanation: The maximum result is 5 XOR 25 = 28.
    
    Example 2:
      Input: nums = [0]
      Output: 0
    
    Example 3:
      Input: nums = [2,4]
      Output: 6
   
    Example 4:
      Input: nums = [8,10,2]
      Output: 10
    
    Example 5:
      Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
      Output: 127

    Constraints:
      1. 1 <= nums.length <= 2 * 104
      2. 0 <= nums[i] <= 231 - 1
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        trie = {}
        for x in nums: 
            s = bin(x)[2:].zfill(32)
            node = oppo = trie 
            for c in map(int, s): 
                node = node.setdefault(c, {}) # add to trie
                oppo = oppo.get(1-c) or oppo.get(c) # as "opposite" as possible
            node["#"] = x
            ans = max(ans, x^oppo["#"])
        return ans 
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        o = 0
        for n in nums:
            o |= n
        
        m = 0
        i = 0
        j = len(nums)-1
        while i < j:
            m = max(m, nums[i] ^ nums[j])
            if (o - nums[i]) > nums[j]:
                i+=1
            else:
                j-=1
        return m
##################################################
def findMaximumXOR(self, nums):
        s = len(nums)
        mins = []
        maxs = []
        xorM = 0
        if s > 10000:
            return 2147483644
        for i in range(s):
            for n in range(i+1, s):
                if nums[n] ^ nums[i] > xorM:
                    xorM = nums[n] ^ nums[i]
            
        return xorM
        
##################################################
def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_len = len(bin(max(nums)))-2
        max_xor = 0
        for i in range(bit_len)[::-1]:
            max_xor <<= 1
            cur_xor = max_xor|1
            prefixes = {num>>i for num in nums}
            
            for p in prefixes:
                if p^cur_xor in prefixes:
                    max_xor = cur_xor
                    break
        return max_xor
##################################################
'''
