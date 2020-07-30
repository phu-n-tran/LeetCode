# --------------------------------------------------------------------------
# Name:        Word Break II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty string s and a dictionary wordDict containing a list 
    of non-empty words, add spaces in s to construct a sentence where each 
    word is a valid dictionary word. Return all such possible sentences.

    Note:
      1. The same word in the dictionary may be reused multiple times in the segmentation.
      2. You may assume the dictionary does not contain duplicate words.
    
    Example 1:
      Input:
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
      Output:
        [
          "cats and dog",
          "cat sand dog"
        ]
    
    Example 2:
      Input:
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
      Output:
        [
          "pine apple pen apple",
          "pineapple pen apple",
          "pine applepen apple"
        ]
      Explanation: Note that you are allowed to reuse a dictionary word.
    
    Example 3:
      Input:
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
      Output:
        []
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {}
        def dfs(i): # return all possibilities in s[i:]
            if i in memo:
                return memo[i]
            else:
                res = []
                for word in wordDict:
                    if i + len(word) == len(s) and word == s[i:i+len(word)]: # reaching the end
                        res.append(word)
                    if i + len(word) < len(s) and word == s[i:i+len(word)]:
                        following_res = dfs(i + len(word)) # getting the suffix and add to the result
                        for following in following_res:
                            res.append(word + " " + following)
                memo[i] = res
                return res
                
            
        return dfs(0)
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def fetch_ans(mp, p, s):
            if p >= len(s):
                return [""]
            ans = []
            for i in mp[p]:
                w = s[p:i]
                for w2 in fetch_ans(mp, i, s):
                    w2 = (" " + w2) if len(w2)>0 else ""
                    ans.append(w+w2)
            return ans
            
        def func(set_words, s):
            mp = defaultdict(lambda : [])
            word_i = [len(s)]
            mp[len(s)] = [len(s)]
            for i in xrange(len(s)-1, -1, -1):
                for j in word_i:
                    if s[i:j] in set_words and mp.has_key(j):
                        mp[i].append(j)
                if mp.has_key(i):
                    word_i.append(i)
            return fetch_ans(mp, 0 , s)
        return func(set(wordDict), s)
                            
                
##################################################
def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        if not n:
            return []
        dp = [[] for _ in range(n)]
        letters1 = set(c for c in s)
        letters2 = set(c for word in wordDict for c in word)
        if not letters2.issuperset(letters1):
            return []
        dic = set(wordDict)
        for i in range(0, n):
            for j in range(0, i + 1):
                cur_word = s[j:i + 1]
                if cur_word in dic:
                    if j == 0:
                        dp[i].append(cur_word)
                    else:
                        for sentence in dp[j - 1]:
                            dp[i].append(sentence + ' ' + cur_word)
        return dp[n - 1]
##################################################
def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        memo = defaultdict(list)
        wordset = set(wordDict)
        result = self.recursive(s,wordset,memo)
        return [" ".join(sentence) for sentence in result]
    def recursive(self, s, wordset, memo):
        if not s:
            return [[]]
        if s in memo:
            return memo[s]
        for i in range(1, len(s)+1):
            word = s[:i]
            if word in wordset:
                for subsentence in self.recursive(s[i:], wordset, memo):
                    memo[s].append([word]+subsentence)
        return memo[s]
 ##################################################
 def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = defaultdict(list)
        wordset = set(wordDict)
        return [" ".join(sentence) for sentence in self.recursive(s, wordset, memo)]
        
    def recursive(self, s, wordset, memo):
        if not s:
            return [[]]
        if s in memo:
            return memo[s]
        for i in range(1, len(s)+1):
            if s[:i] in wordset:
                for subsentence in self.recursive(s[i:],wordset,memo):
                    memo[s].append([s[:i]]+subsentence)
        return memo[s]
        
'''
