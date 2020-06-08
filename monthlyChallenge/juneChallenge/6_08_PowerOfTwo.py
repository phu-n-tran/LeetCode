# --------------------------------------------------------------------------
# Name:        Power Of To
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an integer, write a function to determine if it is a power of two.

    Example 1:
        Input: 1
        Output: true 
        Explanation: 20 = 1
    
    Example 2:
        Input: 16
        Output: true
        Explanation: 24 = 16
    
    Example 3:
        Input: 218
        Output: false
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(100):
            result = 2**i
            if result == n:
                return True
            
            if result > n:
                return False
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return 0
        while n!=1:
            if n%2!=0:
                return False

            n=n//2
        return True

'''
