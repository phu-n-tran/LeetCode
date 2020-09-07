# --------------------------------------------------------------------------
# Name:        Word Pattern
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between
    a letter in pattern and a non-empty word in str.

    Example 1:
      Input: pattern = "abba", str = "dog cat cat dog"
      Output: true
    
    Example 2:
      Input:pattern = "abba", str = "dog cat cat fish"
      Output: false
    
    Example 3:
      Input: pattern = "aaaa", str = "dog cat cat dog"
      Output: false
    
    Example 4:
      Input: pattern = "abba", str = "dog dog dog dog"
      Output: false
    
    Notes:
      1. You may assume pattern contains only lowercase letters, and str
         contains lowercase letters that may be separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split(" ")
        patternDict = {} # key is letter from pattern and value is word from str
        strDict = {} # key is word from str and value is letter from pattern (use to counter example 4)
        
        if len(strList) != len(pattern):
            return False
    
        for i in range(len(pattern)):
            # only add if both dicts does not contain the key
            if pattern[i] not in patternDict and strList[i] not in strDict:
                patternDict[pattern[i]] = strList[i]
                strDict[strList[i]] = pattern[i]
            
            # only need to be mismatch for it to be wrong
            if strList[i] != patternDict.get(pattern[i], "") or pattern[i] != strDict.get(strList[i], ""):
                return False
        
        return True
        
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        sentence = string.split(' ')
        print(sentence)
        if len(sentence) != len(pattern):
            return False
        
        dictionary = dict()
        for i in range(len(pattern)):
            if pattern[i] in dictionary.keys():
                if sentence[i] != dictionary[pattern[i]]:
                    return False
            else:
                if sentence[i] in dictionary.values():
                    return False
                dictionary[pattern[i]] = sentence[i]
        
        
        return True
##################################################
def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        le1=len(pattern)
        ls=str.split(' ')
        le2=len(ls)
        if le1<>le2:
            return False
        dic={}
        for i in range(le1):
            if pattern[i] not in dic:
                if ls[i] not in dic.values():
                    dic[pattern[i]]=ls[i]
                else:
                    return False
            else:
                if dic[pattern[i]]!=ls[i]:
                    return False
        return True
##################################################
def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        stack = [(pattern[0], s[0])]
        for i in range(1, len(pattern)):
            for x, y in stack:
                if (x != pattern[i] and y == s[i]) or (x == pattern[i] and y != s[i]):
                    return False
                if x == pattern[i] and y == s[i]:
                    break
            else:
                stack.append((pattern[i], s[i]))
        return True
##################################################
'''
