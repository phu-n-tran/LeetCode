# --------------------------------------------------------------------------
# Name:        Uncrossed Lines (dynamic programming approach)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary array, find the maximum length of a contiguous subarray
    with equal number of 0 and 1.

    Example 1:
        Input: [0,1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with equal 
                     number of 0 and 1.
        
    Example 2:
        Input: [0,1,0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray 
                     with equal number of 0 and 1.
        
    Note: The length of the given binary array will not exceed 50,000.
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 # sub 1 when read 0, add 1 when read 1
        result = 0
        dic = {0: -1} # use to initialize when the max is from the beginning to the current pos
        
        for i in range(len(nums)):
            curNum = nums[i]
            
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if count in dic:
                result = max(result, i-dic[count]) # take the max of current result withe the distance of current index to the index that the first time that the current value of count has appear
            else:
                dic[count] = i # mark the first time the count appear with the current index
        
        return result
        
        
        ### first time approach: O(N^2)
#         def helper(nums, pos):
#             stack = []
#             result = 0
#             count = 0
#             initNum = nums[pos]
            
#             for i in range(pos, len(nums)):
#                 if not stack:
#                     initNum = nums[i]
#                     count += 1
#                     stack.append(initNum)
#                 elif nums[i] == initNum:
#                     count += 1
#                     stack.append(initNum)
#                 else:
#                     stack.pop()
                
#                 if not stack:
#                     result += count
#                     count = 0
#             return result*2
        
        
#         size = len(nums)
#         if not nums or size == 1:
#             return 0
#         if nums.count(0) == nums.count(1):
#             return size
        
#         return max([helper(nums, i) for i in range(size)])
            
        
        
        
        
          
            
        
 



        
"""other faster methods (from other submissions)
##################################################

"""
