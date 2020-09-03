# --------------------------------------------------------------------------
# Name:        Repeated Substring Pattern
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty string check if it can be constructed by taking a 
    substring of it and appending multiple copies of the substring together.
    You may assume the given string consists of lowercase English letters 
    only and its length will not exceed 10000.

    Example 1:
      Input: "abab"
      Output: True
      Explanation: It's the substring "ab" twice.

    Example 2:
      Input: "aba"
      Output: False

    Example 3:
      Input: "abcabcabcabc"
      Output: True
      Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        SIZE = len(s)
        
        for i in range(1, (SIZE/2)+1):
            if s[:i] * (len(s)//i) == s:
                    return True
            
        # # TLE
        # for i in range(1, (SIZE/2)+1):
        #     pattern = s[0:i]
        #     x = re.findall(pattern, s)
        #     if len(x)*len(pattern) == SIZE:
        #         return True
            
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1] 
##################################################
def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1
##################################################
class Solution(object):
        
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
          return False
        max_len = int(math.sqrt(len(s)))
        if max_len * max_len != len(s):
          max_len += 1
        window_size = max_len
        while window_size > 0:
          if len(s) % window_size == 0:
            size1 = window_size
            size2 = len(s) / window_size

            if self.isRepeated(s, size1):
              return True
            if self.isRepeated(s, size2):
              return True
          window_size -= 1
        return False
      
    def isRepeated(self, s, step):
      prev = s[0:step]
      i = step
      repeated_count = 0
      while(i < len(s)):
        if s[i : i + step] != prev:
          return False
        repeated_count += 1
        i = i + step
      return repeated_count != 0
##################################################
'''
