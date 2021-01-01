# --------------------------------------------------------------------------
# Name:        Remove Duplicate Letters
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string s, remove duplicate letters so that every letter appears 
    once and only once. You must make sure your result is the smallest in 
    lexicographical order among all possible results.

    Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


    Example 1:
      Input: s = "bcabc"
      Output: "abc"
   
    Example 2:
      Input: s = "cbacdcbc"
      Output: "acdb"

    Constraints:
      1_ 1 <= s.length <= 104
      2) s consists of lowercase English letters.
      
    Hint:
      1) Greedily try to add one missing character. How to check if 
         adding some character will not cause problems ? Use bit-masks to 
         check whether you will be able to complete the sub-sequence if you 
         add the character at some index i.
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #????
#         import re
#         letterList = re.split(r"(\w)", s)
#         uniqueSet = set(letterList)

#         return "".join(sorted(uniqueSet))
        lastPos = {}
        for i in range(len(s)): lastPos[s[i]] = i
        stack = []
        seen= set()
        for i in range(len(s)):
            if s[i] in seen: continue
            while stack and stack[-1] > s[i] and lastPos[stack[-1]] > i:
                p = stack.pop()
                seen.remove(p)
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
##################################################
##################################################
##################################################
'''
