# --------------------------------------------------------------------------
# Name:        Combination Sum III
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Find all possible combinations of k numbers that add up to a number n,
    given that only numbers from 1 to 9 can be used and each combination 
    should be a unique set of numbers.

    Note:
      1. All numbers will be positive integers.
      2. The solution set must not contain duplicate combinations.
    
    Example 1:
      Input: k = 3, n = 7
      Output: [[1,2,4]]
    
    Example 2:
      Input: k = 3, n = 9
      Output: [[1,2,6], [1,3,5], [2,3,4]]
      
    https://leetcode.com/problems/combination-sum-iii/solution/
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(digit, start_num, cur, cur_sum):
            if cur_sum == n and digit == k: ans.append(cur[:])
            elif digit >= k or cur_sum > n: return    
            else:
                for i in range(start_num+1, 10):
                    cur.append(i)
                    dfs(digit+1, i, cur, cur_sum+i)
                    cur.pop()
        ans = list()
        dfs(0, 0, [], 0)
        return ans
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.dfs(candidates, 0, res, [], k, n)
        return res
    
    def dfs(self, nums, index, res, path, k, n):
        if k == 0 and n == 0:
            res.append(path)
            return
        if k < 0 or n < 0:
            return 
        
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, res, path + [nums[i]], k-1, n-nums[i])
##################################################
def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def bt(i, arr):
            if len(arr) == k and sum(arr) == n:
                res.append(arr)
                return
            if len(arr) >= k:
                return
            
            for j in range(i, 10):
                bt(j+1, arr+[j])
            
        bt(1, [])
        return res
##################################################
def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(nums, idx, ans, sum):
            if sum < 0: return
            if len(ans) == k and sum == 0:
                res.append(ans)
                return 
            for i in range(idx, len(nums)):
                helper(nums, i+1, ans+[nums[i]], sum-nums[i])
                
        res = []
        helper(range(1,10), 0,[], n)
        return res
##################################################
def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                result.append(list(comb))
                return
            if remain < 0  or len(comb) == k:
                return
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain - (i+1), comb, i+1)
                comb.pop()
        backtrack(n,[],0)
        
        return result
'''
