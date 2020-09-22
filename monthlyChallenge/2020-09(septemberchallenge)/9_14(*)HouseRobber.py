# --------------------------------------------------------------------------
# Name:        House Robber
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint 
    stopping you from robbing each of them is that adjacent houses have 
    security system connected and it will automatically contact the police
    if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money
    of each house, determine the maximum amount of money you can rob tonight 
    without alerting the police.


    Example 1:
      Input: nums = [1,2,3,1]
      Output: 4
      Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.
    
    Example 2:
      Input: nums = [2,7,9,3,1]
      Output: 12
      Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                   Total amount you can rob = 2 + 9 + 1 = 12.

    Constraints:
      1. 0 <= nums.length <= 100
      2. 0 <= nums[i] <= 400
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)          
        return dp2 
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for idx, val in enumerate(nums[1:]):
            idx += 2
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + val)
            
        return dp[-1]
##################################################
class Solution(object):
    def __init__(self):
        self.lookup = dict()
        
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in self.lookup:
            return self.lookup[len(nums)]
        profit1 = 0
        profit2 = 0
        if nums:
            profit1 = nums[0]
        if len(nums) >= 2:
            profit2 = nums[1]
        if len(nums) >= 3:
            profit1 += self.rob(nums[2:])
        if len(nums) >= 4:
            profit2 += self.rob(nums[3:])
        self.lookup[len(nums)] = max(profit1, profit2)
        return max(profit1, profit2)
##################################################
def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <=2:
            return max(nums)
        dp = [0] * (len(nums))

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i] + dp[i-2])
            
        return (dp[-1])
##################################################
'''
