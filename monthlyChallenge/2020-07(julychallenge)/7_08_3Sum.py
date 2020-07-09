# --------------------------------------------------------------------------
# Name:        3 Sum
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array nums of n integers, are there elements a, b, c in nums 
    such that a + b + c = 0? Find all unique triplets in the array which
    gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.

    Example:
      Given array nums = [-1, 0, 1, 2, -1, -4],
      A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
     
     Hints:
      1. So, we essentially need to find three numbers x, y, and z such
         that they add up to the given value. If we fix one of the numbers 
         say x, we are left with the two-sum problem at hand!
      2. For the two-sum problem, if we fix one of the numbers, say
          x
          , we have to scan the entire array to find the next number
          y
          which is
          value - x
          where value is the input parameter. Can we change our array somehow so that this search becomes faster?
      3. The second train of thought for two-sum is, without changing 
         the array, can we use additional space somehow? Like maybe a
         hash map to speed up the search?
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def threeSum(self,n):
        a = []
        c = {}
        for m in n:
            if m in c:
                c[m] += 1
            else:
                c[m] = 1
        n = sorted(c)
        for i, v in enumerate(n):
            if v == 0:
                if c[v] >= 3:
                    a.append([0, 0, 0])
            elif c[v] >= 2 and -2*v in c:
                a.append([v, v, -2*v])
            if v < 0:
                t = -v
                l=bisect.bisect_left(n,(t-n[-1]),i+1)
                r=bisect.bisect_right(n,(t//2),l)
                for x in n[l:r]:
                    y=t-x
                    if y in c and y!=x:
                        a.append([v,x,y])
        return a
##################################################

##################################################

'''
