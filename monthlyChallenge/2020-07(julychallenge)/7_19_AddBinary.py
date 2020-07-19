# --------------------------------------------------------------------------
# Name:        Add Binary
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:
      Input: a = "11", b = "1"
      Output: "100"
    
    Example 2:
      Input: a = "1010", b = "1011"
      Output: "10101"

    Constraints:
      1. Each string consists only of '0' or '1' characters.
      2. 1 <= a.length, b.length <= 10^4
      3. Each string is either "0" or doesn't contain any leading zero.
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ""
        
        # use a
        if len(a) > len(b):
            for i in range(-1, (len(a)+1)*-1, -1):
                if i*-1 > len(b):
                    temp = int(a[i]) + carry
                else:                   
                    temp = int(a[i]) + int(b[i]) + carry
                    
                if temp == 3:
                    result = "1" + result
                    carry = 1
                elif temp == 2:
                    result = "0" + result
                    carry = 1
                elif temp == 1:
                    result = "1" + result
                    carry = 0
                else:
                    result = "0" + result
                    carry = 0
            if carry == 1:
                result = "1" + result
        else: # use b
            for i in range(-1, (len(b)+1)*-1, -1):
                if i*-1 > len(a):
                    temp = int(b[i]) + carry
                else:                   
                    temp = int(a[i]) + int(b[i]) + carry
                    
                if temp == 3:
                    result = "1" + result
                    carry = 1
                elif temp == 2:
                    result = "0" + result
                    carry = 1
                elif temp == 1:
                    result = "1" + result
                    carry = 0
                else:
                    result = "0" + result
                    carry = 0
            if carry == 1:
                result = "1" + result
            
                
        return result
            
        

            
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
##################################################
def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return "{:b}".format(int(a,2)+int(b,2))
##################################################
def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        x = int(a, 2)
        y = int(b, 2)
        
        while y:
            x, y = x^y, (x&y)<<1 #x: sum, y: carry
        return bin(x)[2:]
##################################################
def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = max(len(a), len(b))
        
        a = a.zfill(l)
        b = b.zfill(l)
        
        res = ''
        
        c = 0
        
        for i in range(l - 1, -1, -1):
            r = c
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            res = ('1' if r % 2 == 1 else '0') + res
            c = 0 if r < 2 else 1
            
        if c != 0:
            res = '1' + res
            
        return res
'''
