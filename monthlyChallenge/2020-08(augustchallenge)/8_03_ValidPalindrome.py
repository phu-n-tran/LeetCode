
# --------------------------------------------------------------------------
# Name:        Valid Palindrome
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string, determine if it is a palindrome, considering only 
    alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:
      Input: "A man, a plan, a canal: Panama"
      Output: true
    
    Example 2:
      Input: "race a car"
      Output: false

    Constraints:
      1. s consists only of printable ASCII characters.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        low = 0
        high = len(s) - 1
        
        while low < high:
            if s[low] != s[high]:
                return False
            
            low += 1
            high -= 1
        
        return True
        
        
        
        
        
        
        
    
        
            
        


        
'''other faster methods (from other submissions)
##################################################
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        
        s = ''.join(e for e in s if e.isalnum())
        s = s.lower()
        return s == s[::-1]
##################################################
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0
        # s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        back = len(s)-1
        while front < back:
            if s[front]==s[back]:
                front += 1
                back -= 1
            else:
                return False
        return True
##################################################
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ns = re.sub("[^a-zA-Z0-9]","",s).lower()
        return ns == ns[::-1]
'''
