# --------------------------------------------------------------------------
# Name:        Largest Divisible Subset
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a set of distinct positive integers, find the largest subset such
    that every pair (Si, Sj) of elements in this subset satisfies:

    Si % Sj = 0 or Sj % Si = 0.

    If there are multiple solutions, return any subset is fine.

    Example 1:
        Input: [1,2,3]
        Output: [1,2] (of course, [1,3] will also be ok)
    
    Example 2:
        Input: [1,2,4,8]
        Output: [1,2,4,8]
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums:
            nums.sort()
            results = [[each_ele] for each_ele in nums]

            for i in range(len(nums)):
                for k in range(i):
                    # 1st cond is to check if the current number divisible by all the small number
                    # 2nd cond is to make sure the iterate number is also divisible by other numbers in the list
                    if nums[i] % nums[k] == 0 and len(results[i]) <= len(results[k]):
                        results[i] += [nums[k]]
            print(results)
            
            # return max(results, key=len)
            return max(results, key=lambda each_list: len(each_list))
        
        
        
        
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        dic = {}
        for i in sorted(nums):
            a = [(k,len(dic[k])) for k in dic if i%k==0]
            #print(dic)
            if a:
                dic[i]=dic[max(a,key=lambda x:x[1])[0]]+[i]
            else:
                dic[i]=[i]
        #print(dic)
        return max(dic.items(), key=lambda x:len(x[1]))[1]
'''
