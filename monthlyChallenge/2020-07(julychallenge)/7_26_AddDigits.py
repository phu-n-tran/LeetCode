# --------------------------------------------------------------------------
# Name:        Add Digits
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-negative integer num, repeatedly add all its digits until
    the result has only one digit.

    Example:
      Input: 38
      Output: 2 
      Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
                   Since 2 has only one digit, return it.
                 
    Follow up:
      Could you do it without any loop/recursion in O(1) runtime?
      
    Hints:
      1. A naive implementation of the above process is trivial. Could you
         come up with other methods?
      2. What are all the possible results?
      3. How do they occur, periodically or randomly?
      4. You may find this Wikipedia article useful.
      
    #########  
    # NOTE  # resolve around 9
    #########
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def helper(digits, pos, carry):
            if pos < 0:
                digits.insert(0, 1)
                return
            
            digits[pos] += carry
            if digits[pos] > 9:
                digits[pos] = 0;
                carry = 1
                return helper(digits, pos-1, carry)
            
        helper(digits, len(digits)-1, 1)
        return digits
        
        # if num == 0:
        #         return 0
        #     if num % 9 == 0:
        #         return 9
        #     return num % 9
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        """
        while num // 10 > 0:
            digits = []
            while num > 0:
                digits.append(num%10)
                num //= 10
            if len(digits) == 0:
                digits.append(0)
            # print(digits)
            num = sum(digits)
        return num
        """
        
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
##################################################
def addDigits(self, num):
        sum = num
        rem =0
        while(sum>=10):
            sum = 0
            while(num!=0):
                rem = num%10
                sum += rem
                num = num/10
            num = sum
        return sum
##################################################
def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        r = num % 9
        if r == 0 and num > 0:
            r = 9
        return r
'''
