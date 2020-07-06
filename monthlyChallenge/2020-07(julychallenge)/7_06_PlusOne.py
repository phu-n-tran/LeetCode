# --------------------------------------------------------------------------
# Name:        Plus One
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty array of digits representing a non-negative integer, 
    plus one to the integer.

    The digits are stored such that the most significant digit is at the head
    of the list, and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the 
    number 0 itself.

    Example 1:
      Input: [1,2,3]
      Output: [1,2,4]
      Explanation: The array represents the integer 123.
    
    Example 2:
      Input: [4,3,2,1]
      Output: [4,3,2,2]
      Explanation: The array represents the integer 4321.
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
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def plusOne(self, digits):
        res = []
        carry = 1
        for i in range (len(digits) - 1, -1, -1):
            digits[i]=digits[i]+carry
            if(digits[i]>=10):
                digits[i]=0
                carry=1
            else:
                break;
        if(digits[0]==0):
            digits.insert(0,1)
        
        
        return digits
##################################################
def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]<9):
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits
##################################################
def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        n = len(digits)
        for i in range(n-1, -1, -1):
            s = (digits[i] + 1) % 10
            carry = (digits[i] + 1) / 10
            digits[i] = s
            if not carry:
                break
        if carry:
            digits.insert(0, carry)
        return digits
'''
