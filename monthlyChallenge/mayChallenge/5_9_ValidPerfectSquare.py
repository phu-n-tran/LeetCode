# --------------------------------------------------------------------------
# Name:        Valid Perfect Square
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a positive integer num, write a function which returns True if 
    num is a perfect square else False.
    
    Example 1:
        Input: 16
        Output: true
    
    Example 2:
        Input: 14
        Output: false
        
    Note: Do not use any built-in library function such as sqrt.
"""
import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        size = float(len(str(num)))
        bound = int(math.ceil(size/2))

        upper = int("9"+"9"*(bound-1))
        lower = int("1"+"0"*(bound-1))
        
        return self.binary_check(lower, upper, num)
       
    def binary_check(self, lower, upper, value):
        if lower <= upper:
            mid = lower + (upper-lower)//2
            
            if mid**2 == value:
                return True
            elif mid**2 > value:
                return self.binary_check(lower, mid-1, value)
            else:
                return self.binary_check(mid+1, upper, value)
        return False

            







        
"""other faster methods (from other submissions)
##################################################
def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            print(x)
            x = (x + num / x) // 2
            print(x)
            print("--")

        return x * x == num

"""
