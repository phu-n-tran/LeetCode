# --------------------------------------------------------------------------
# Name:        Is Subsequence
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string s and a string t, check if s is subsequence of t.

    A subsequence of a string is a new string which is formed from the 
    original string by deleting some (can be none) of the characters without
    disturbing the relative positions of the remaining characters. 
    (ie, "ace" is a subsequence of "abcde" while "aec" is not).

    Follow up:
        If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
        and you want to check one by one to see if T has its subsequence.
        In this scenario, how would you change your code?
        
    Example 1:
        Input: s = "abc", t = "ahbgdc"
        Output: true
    
    Example 2:
        Input: s = "axc", t = "ahbgdc"
        Output: false
    
    Constraints:
        1. 0 <= s.length <= 100
        2. 0 <= t.length <= 10^4
        3. Both strings consists only of lowercase characters.
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        size_s = len(s)
        iter_s = 0
        
        for i in range(len(t)):
            if iter_s > size_s-1:
                return True
                
            if t[i] == s[iter_s]:
                iter_s += 1
        
        if iter_s > size_s-1:
                return True
        return False
            
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
##################################################
def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        total_len = len(t)
        p = 0
        if len(s) == 0 or s==t:
            return True
        if total_len != 0:
            for i in range(0, total_len):
                if t[i] == s[p]:
                    p += 1
                if p==len(s):
                    break
            if p==len(s):
                return True
        return False
'''
