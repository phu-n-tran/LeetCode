# --------------------------------------------------------------------------
# Name:        Subsets
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Example:
      Input: nums = [1,2,3]
      Output:
        [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.out = []
        self.dfs([-1],nums)
        return self.out

    def dfs(self, current, nums):
        self.out.append([nums[s] for s in current][1:])
        for i in range(current[-1] + 1, len(nums)):
            self.dfs(current + [i], nums)
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #dfs
        res=[]
        self.dfs(nums,res,[],0)
        
        return res
    def dfs(self,nums,res,now,index):
        res.append(now)
        #print(res)
        for i in range(index,len(nums)):

            self.dfs(nums,res,now+[nums[i]],i+1)
        
        '''
        #backtrack
        res=[]
        self.backtrack(nums,res,[],0)
        
        return res
    def backtrack(self,nums,res,now,index):
        res.append(now[:])
        #print(res)
        for i in range(index,len(nums)):
            now.append(nums[i])
            self.backtrack(nums,res,now,i+1)
            now.pop()
        '''
        '''
        #like DP 2 is the result from 1+2, 3 is the result from1,2 +3
        #time: O(n*2^n) space:O(n*2^n)
        output=[[]]
        
        for num in nums:
            for i in range(len(output)):
                output.append(output[i]+[num])
                #print(output)    
        return output
        '''
                
##################################################
def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        n = len(nums)
        
        sets = self.subsets(nums[: n - 1])
        nsets = len(sets)
        
        for i in range(nsets):
            sets.append(sets[i] + [nums[n-1]])
            
        return sets
##################################################
def subsets(self, nums):
        
        def dfs(nums, index, ans, curr):
            ans.append(curr)
            for i in xrange(index, len(nums)):
                dfs(nums, i+1, ans, curr+[nums[i]])
            return ans 
        return dfs(nums, 0, [], [])
'''
