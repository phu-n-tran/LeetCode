# --------------------------------------------------------------------------
# Name:        Length of Last Word
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string s consists of upper/lower-case alphabets and empty space
    characters ' ', return the length of last word (last word means the last
    appearing word if we loop from left to right) in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a maximal substring consisting of non-space characters only.

    Example:
      Input: "Hello World"
      Output: 5
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # test "a ks  " => 2
        return len(s.rstrip().split(" ")[-1])
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s.strip():
            return 0
        return len(s.split()[-1])
##################################################
def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_arr = s.split()
        if len(str_arr) == 0: return 0
        else: return len(str_arr[-1])
##################################################
def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        i = len(s)-1
        
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1
            
        return cnt
##################################################
'''
