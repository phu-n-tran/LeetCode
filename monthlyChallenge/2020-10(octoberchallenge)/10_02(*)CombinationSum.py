
# --------------------------------------------------------------------------
# Name:        Combination Sum
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen 
    numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. 
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    It is guaranteed that the number of unique combinations that sum up to 
    target is less than 150 combinations for the given input.
    

    Example 1:
      Input: candidates = [2,3,6,7], target = 7
      Output: [[2,2,3],[7]]
      Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
    
    Example 2:
      Input: candidates = [2,3,5], target = 8
      Output: [[2,2,2,2],[2,3,3],[3,5]]
    
    Example 3:
      Input: candidates = [2], target = 1
      Output: []

    Example 4:
      Input: candidates = [1], target = 1
      Output: [[1]]

    Example 5:
      Input: candidates = [1], target = 2
      Output: [[1,1]]

    Constraints:
      1. 1 <= candidates.length <= 30
      2. 1 <= candidates[i] <= 200
      3. All elements of candidates are distinct.
      4. 1 <= target <= 500
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates) # sort to terminate early when target < 0
        
        def backtracking(i, target, path):
            if target == 0:
                ans.append(path)
                return
            if i == len(candidates) or target < candidates[i]:
                return
            backtracking(i, target - candidates[i], path + [candidates[i]]) # Choose ith candidate
            backtracking(i + 1, target, path) # Skip ith candidate
        
        ans = []
        backtracking(0, target, [])
        return ans
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ans = []
        
        def dfs(nums,currSet,currSum):
            for i in range(len(nums)):
                tempSum = nums[i]+currSum
                
                if tempSum == target:
                    ans.append(currSet + [nums[i]])
                
                elif tempSum > target:
                    return
                
                else:
                    dfs(nums[i:],currSet+[nums[i]],tempSum)
        dfs(candidates,[],0)
        
        return ans
##################################################
def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return 

            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result
##################################################
def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        candidates.sort()
        
        def _dfs(ls, remain, path):
            if remain == 0:
                combinations.append(path)
            for i, num in enumerate(ls):
                if num > remain:
                    break
                _dfs(ls[i:], remain - num, path + [num])
        
        _dfs(candidates, target, [])
        return combinations
            
##################################################
'''
