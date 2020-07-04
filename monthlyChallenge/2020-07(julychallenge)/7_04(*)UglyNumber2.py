# --------------------------------------------------------------------------
# Name:        Ugly Number 2
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
   Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

    Example:
      Input: n = 10
      Output: 12
      Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
    
    Note:  
      1. 1 is typically treated as an ugly number.
      2. n does not exceed 1690.

    Hints:
     1. The naive approach is to call isUgly for every number until you reach the nth one. 
        Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
     2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
     3. The key is how to maintain the order of the ugly numbers. Try a similar approach of 
        merging from three sorted lists: L1, L2, and L3.
     4. Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*n
        i2,i3,i5=0,0,0
        n2=2
        n3=3
        n5=5
        dp[0]=1
        for i in range (1,n):
            dp[i]=min(n2,n3,n5)
            if n2==dp[i]:
                i2+=1
                n2=2*dp[i2]
            if n3==dp[i]:
                i3+=1
                n3=3*dp[i3]
            if n5==dp[i] :
                i5+=1
                n5=5*dp[i5]
        return dp[n-1]  
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]
##################################################
class Ugly:
    def __init__(self):
        seen = {1, }
        self.nums = nums = []
        heap = []
        heappush(heap, 1)
        
        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
        

class Solution(object):
    u = Ugly()
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.u.nums[n-1]
##################################################
def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N > 14 :
            N %= 14
            
        if N %14 == 0:
            N = 14
     
        for i in range(N):
            cur = [0] * 8
            for j in range(1,7):
                if cells[j-1] == cells[j+1]:
                    cur[j] = 1
                else:
                    cur[j] = 0
            cells = cur
 
        return cur
'''
