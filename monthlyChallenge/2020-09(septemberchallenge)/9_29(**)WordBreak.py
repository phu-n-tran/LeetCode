# --------------------------------------------------------------------------
# Name:        Word Break
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty string s and a dictionary wordDict containing a list
    of non-empty words, determine if s can be segmented into a space-separated 
    sequence of one or more dictionary words.

    Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    
    Example 1:
      Input: s = "leetcode", wordDict = ["leet", "code"]
      Output: true
      Explanation: Return true because "leetcode" can be segmented as "leet code".
    
    Example 2:
      Input: s = "applepenapple", wordDict = ["apple", "pen"]
      Output: true
      Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                   Note that you are allowed to reuse a dictionary word.
    Example 3:
      Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #https://www.youtube.com/watch?v=tSbBuiO1rXI
        dp = [True] + [False] * len(s)
        
        for indx in range(1, len(s) + 1):
            
            for word in wordDict:
                if dp[indx - len(word)] and s[:indx].endswith(word):
                    dp[indx] = True
            
        return dp[-1]
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memory= {"":True}
        def backtrack(s):
            if s in memory:
                return memory[s]
            ans = False
            for word in wordDict:
                if s[:len(word)] == word:
                    ans = ans or backtrack(s[len(word):])
                if ans:
                    return ans
            memory[s] = ans
            return ans
        return backtrack(s)
##################################################
def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        splittable = [False] * (len(s) + 1)
        splittable[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and splittable[i - len(word)] and s[i - len(word):i] == word:
                    splittable[i] = True
                    break 
        
        return splittable[len(s)]
##################################################
def wordBreak(self, s, wordDict):
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if (w == s[i-len(w)+1:i+1]):
                    if(d[i-len(w)] or i-len(w) == -1):
                        d[i] = True
        return d[len(d)-1]
##################################################
'''
