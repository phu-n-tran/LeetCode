# --------------------------------------------------------------------------
# Name:        Power of Four
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

    Example 1:
      Input: 16
      Output: true
    
    Example 2:
      Input: 5
      Output: false
    
    Follow up: Could you solve it without loops/recursion?
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num < 1:
            return False
        
        if num == 1:
            return True
        
        if num % 4 == 0:
            return self.isPowerOfFour(num / 4)
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        while num%4 == 0:
            print num
            num /= 4
            if num < 4:
                break
                
        print num
        if num != 1:
            return False

        return True
##################################################
def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and (1073741824 % num == 0) and (num - 1) % 3 == 0 
##################################################
def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num % 4 == 0 and num != 0:
            num /= 4
        return num == 1
##################################################
def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        mask = 0x55555555
        if num & (num-1) != 0: return False
        return mask & num != 0
'''
