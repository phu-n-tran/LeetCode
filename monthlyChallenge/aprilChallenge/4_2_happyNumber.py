# --------------------------------------------------------------------------
# Name:        Happy Number
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Write an algorithm to determine if a number n is "happy".

    A happy number is a number defined by the following process: Starting 
    with any positive integer, replace the number by the sum of the squares 
    of its digits, and repeat the process until the number equals 1 
    (where it will stay), or it loops endlessly in a cycle which does not 
    include 1. Those numbers for which this process ends in 1 are happy numbers.
    
    A number will not be a Happy Number when it makes a loop in its sequence 
    that is it touches a number in sequence which already been touched.

    Return True if n is a happy number, and False if not.
    
    Example 1:
        Input: 19
        Output: true
        Explanation: 
          12 + 92 = 82
          82 + 22 = 68
          62 + 82 = 100
          12 + 02 + 02 = 1
    
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        unique = set()
        
        while True:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            n = sum
            
            if n == 1 or n in unique:
                break
                
            unique.add(n)
        return n == 1


"""other faster methods (from other submissions)
##################################################
def sum_of_squares(num):
            sum = 0
            while num!=0:
                sum+= pow(num%10,2)
                num = num / 10
            return sum
        
class Solution(object):
    def isHappy(self, num):
        """
        :type n: int
        :rtype: bool
        """
        while num not in [2,3,4,5,6]:
            num = sum_of_squares(num)
            if num == 1:
                return True
        return False
"""
