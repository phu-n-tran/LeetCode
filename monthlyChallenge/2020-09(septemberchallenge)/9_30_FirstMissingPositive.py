# --------------------------------------------------------------------------
# Name:        First Missing Positive
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an unsorted integer array, find the smallest missing positive integer.

    Example 1:
      Input: [1,2,0]
      Output: 3
    
    Example 2:
      Input: [3,4,-1,1]
      Output: 2
    
    Example 3:
      Input: [7,8,9,11,12]
      Output: 1
    
    Follow up:
      Your algorithm should run in O(n) time and uses constant extra space.
    
    Hints:
      1. Think about how you would solve the problem in non-constant space. 
         Can you apply that logic to the existing space?
      2. We don't care about duplicates or non-positive integers
      3. Remember that O(2n) = O(n)
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         if not nums:
#             return 1
        
#         for i in range(1, len(nums)+2):
#             if i not in nums:
#                 return i
######## OR
        nums.sort()
        result = 1
        
        for i in nums:
            if i == result:
                result += 1
            if result < i:
                break
        return result
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n
##################################################
def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 1
        else:
            hashm=dict.fromkeys(nums)
            maxi=nums[-1]
            
            for i in range(len(nums)):
                if nums[i]>maxi:
                    maxi=nums[i]
            if maxi<0:
                return 1
            k=0
            while k < maxi:
                if k not in hashm and k!=0:
                    return k
                k=k+1
            return maxi+1
##################################################
def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num <= 0 or num > n:
                continue
            if num == n:
                t = nums[0]
                nums[0] = n
                #nums[i] = t
                self.putNum(nums, i, t)
                continue
                
            t = nums[num]
            nums[num] = num
            #nums[i] = t
            #print "1 i %s t %s nums %s" %(i, t, nums)
            self.putNum(nums, i, t)
            #print "2 i %s nums %s" %(i, nums)
        
        for i in range(1, n):
            if nums[i] != i:
                return i
            
        if nums[0] != n:
            return n
        return n+1
    
    def putNum(self, nums, i, n):
        while True:
            if n <= 0 or n > len(nums):
                break
            if n == len(nums):
                t = nums[0]
                nums[0] = n
            else:
                t = nums[n]
                #print "Put num t %s n %s nums %s" %(t, n,nums)
                nums[n] = n
            if t == n:
                break
            n = t
##################################################
'''
