# --------------------------------------------------------------------------
# Name:        Excel Sheet Column Number
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...

    Example 1:
      Input: "A"
      Output: 1

    Example 2:
      Input: "AB"
      Output: 28

    Example 3:
      Input: "ZY"
      Output: 701

    Constraints:
      1. 1 <= s.length <= 7
      2. s consists only of uppercase English letters.
      3. s is between "A" and "FXSHRXW".
      
    My approach:
      - first add the value of the first letter
      - then everytime, we move to the next letter, 
          mul by 26 (since there are 26 letters) and then 
          add the value of that current letter (e.g. "A" = 1)
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store the value of the first letter
        result = ord(s[0]) - 64
        
        # if there are more than one letter
        for i in range(1, len(s)):
            # mul result by 26 each time move to a new letter
            # then add the value of the current letter
            result *= 26
            result += ord(s[i]) - 64
            
        return result
#         result = 0
#         # print(ord("C") - 64)
        
#         for letter in s:
#             result += ord(letter) - 64
#             result *= 26
            
#         return result/26
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def titleToNumber(self, s):
        to = 0
        for i in range(len(s)):
            oo = ord(s[i])-64
            to+=(oo)*(26**(len(s)-i-1))
        return to  
##################################################
def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://blog.csdn.net/coder_orz/article/details/51406455
        # ord(c): return an integer representing the Unicode of that character 
        # chr(i): return the string representing a character whose Unicode is the integer i
        
        sum = 0
        for c in s:
            sum = sum * 26 + ord(c) - ord('A') + 1 # ord('A') = 65
            
        return sum
##################################################
def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total = 0
        
        for i in range(0, len(s)):
            char = s[~i]
            encoding = (ord(char) - 64) * max(1, (26 ** i))
            
            total += encoding
        
        return total
'''
