# --------------------------------------------------------------------------
# Name:        First Unique Character in String
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two words word1 and word2, find the minimum number of operations 
    required to convert word1 to word2.

    You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
    
    Example 1:
        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation: 
            horse -> rorse (replace 'h' with 'r')
            rorse -> rose (remove 'r')
            rose -> ros (remove 'e')
            
    Example 2:
        Input: word1 = "intention", word2 = "execution"
        Output: 5
        Explanation: 
            intention -> inention (remove 't')
            inention -> enention (replace 'i' with 'e')
            enention -> exention (replace 'n' with 'x')
            exention -> exection (replace 'n' with 'c')
            exection -> execution (insert 'u')
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1, word2 = "_" + word1, "_" + word2
        dp = [[0] * len(word2) for _ in range(len(word1))]

        for i in range(len(word1)): 
            dp[i][0] = i
        for j in range(len(word2)): 
            dp[0][j] = j

        for i in range(1, len(word1)):
            for j in range(1,len(word2)):
                dis = (word1[i] != word2[j])
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + dis)

        return dp[-1][-1]
        
        
        
        
        
        
"""other faster methods (from other submissions)
##################################################
def search(s, t, i, j, d):
    if i == 0:
        return j
    if j == 0:
        return i
    
    if (i, j) in d:
        return d[(i, j)]

    d[(i, j)] = search(s, t, i - 1, j - 1, d) if s[i-1] == t[j-1] \
        else min(search(s, t, i, j - 1, d), 
                 search(s, t, i - 1, j, d), 
                 search(s, t, i - 1, j - 1, d)) + 1

    return d[(i, j)]


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        return search(word1, word2, len(word1), len(word2), dict())
"""
