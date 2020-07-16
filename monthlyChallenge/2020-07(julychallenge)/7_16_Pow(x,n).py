# --------------------------------------------------------------------------
# Name:        Pow(x, n)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Implement pow(x, n), which calculates x raised to the power n (x^n).

    Example 1:
      Input: 2.00000, 10
      Output: 1024.00000
    
    Example 2:
      Input: 2.10000, 3
      Output: 9.26100
    
    Example 3:
      Input: 2.00000, -2
      Output: 0.25000
      Explanation: 2-2 = 1/22 = 1/4 = 0.25
    
    Note:
      1. -100.0 < x < 100.0
      2. n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other  methods (from other submissions)
##################################################
def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x=1./x
            n =-n
        v = 1
        while n>0:
            s = n%2
            if s>0:
                v *= x
            n = n/2
            x = x*x
        return v
##################################################
def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            x=float(1/x)
            n=n*-1
        
        if n%2==0:
            ans=self.myPow(x,n//2)
            return ans**2
        else:
            ans=self.myPow(x,n//2)
            return (ans**2)*self.myPow(x,n%2)
##################################################

'''
