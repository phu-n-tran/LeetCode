# --------------------------------------------------------------------------
# Name:        First Unique Character in String
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string, find the first non-repeating character in it and return 
    it's index. If it doesn't exist, return -1.
    
    Example 1:
        s = "leetcode"
        return 0.
    
    Example 2:
        s = "loveleetcode",
        return 2.
    
    Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterSet = set()
        
        for letter in s:
            if letter not in letterSet and s.count(letter) == 1:
                return s.index(letter)
            letterSet.add(letter)
        return -1
        
        
        
        
        
"""other faster methods (from other submissions)
##################################################
letters='abcdefghijklmnopqrstuvwxyz'
index=[s.index(l) for l in letters if s.count(l) == 1]
return min(index) if len(index) > 0 else -1
#################################################
"""
