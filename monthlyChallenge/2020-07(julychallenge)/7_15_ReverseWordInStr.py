# --------------------------------------------------------------------------
# Name:        Reverse Words in a String
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an input string, reverse the string word by word.

    Example 1:
      Input: "the sky is blue"
      Output: "blue is sky the"
    
    Example 2:
      Input: "  hello world!  "
      Output: "world! hello"
      Explanation: Your reversed string should not contain leading or trailing spaces.
    
    Example 3:
      Input: "a good   example"
      Output: "example good a"
      Explanation: You need to reduce multiple spaces between two words 
                   to a single space in the reversed string.

    Note:
      1. A word is defined as a sequence of non-space characters.
      2. Input string may contain leading or trailing spaces. However, your
         reversed string should not contain leading or trailing spaces.
      3. You need to reduce multiple spaces between two words to a single space
         in the reversed string.

    Follow up:
      For C programmers, try to solve it in-place in O(1) extra space.
"""


import re

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newstr = re.sub('\s+', ' ', s)
        return " ".join(newstr.strip().split(" ")[::-1])
        
        # or
        # return " ".join(s.split()[::-1])
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return " ".join(reversed(s.strip().split()))
##################################################
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
##################################################
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''.join([])
        words = s.split()
        return ' '.join(reversed(words))
##################################################
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.reverseWords2(s)
    
    def reverseWords2(self, s):
        return " ".join(reversed(s.split()))
        
        
    def reverseWords1(self, s):
        s = s.strip(' ')
        queue = collections.deque()
        left = 0
        for i, c in enumerate(s):
            if i > 0 and s[i - 1] == ' ': left = i
            if i == len(s) - 1 or (s[i + 1] == ' ' and s[i] != ' '):
                queue.appendleft(s[left : i + 1])
            
        return " ".join(queue)
'''
