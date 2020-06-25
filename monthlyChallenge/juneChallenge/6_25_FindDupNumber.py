# --------------------------------------------------------------------------
# Name:        Find the Duplicate Number
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array nums containing n + 1 integers where each integer is 
    between 1 and n (inclusive), prove that at least one duplicate number
    must exist. Assume that there is only one duplicate number, find the
    duplicate one.

    Example 1:
      Input: [1,3,4,2,2]
      Output: 2
    
    Example 2:
      Input: [3,1,3,4,2]
      Output: 3
    
    Note:
      1. You must not modify the array (assume the array is read only).
      2. You must use only constant, O(1) extra space.
      3. Your runtime complexity should be less than O(n2).
      4. There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        
        for i in nums:
            if d.get(i):
                return i
            else:
                d[i] = 1
        
        
        
        
        
        
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
#################################################
def findDuplicate(self, nums):
        slow = fast = tmp = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break  
        while 1:
            slow = nums[slow]
            tmp = nums[tmp]
            if tmp == slow: break
        return slow
#################################################
def findDuplicate(self, nums):
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                return num
            else:
                nums[num-1] = -nums[num-1]
'''
