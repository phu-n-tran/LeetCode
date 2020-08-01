# --------------------------------------------------------------------------
# Name:        Detect Capital
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a word, you need to judge whether the usage of capitals in it is right or not.

    We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Otherwise, we define that this word doesn't use capitals in a right way.

    Example 1:
      Input: "USA"
      Output: True

    Example 2:
      Input: "FlaG"
      Output: False

    Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1 or word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower()):
            return True
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        elif word[0].isupper() & word[1:].islower():
            return True
        elif word.islower():
            return True
        else:
            return False
##################################################
def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if(len(word) <= 1): return True
        
        if(self.checkAllUpper(word) or self.checkAllLower(word)): return True 
        
        if(word[0].isupper()):
            if self.checkAllLower(word[1:]) or self.checkAllUpper(word[1:]):
                return True
            
        return False
            
        
    def checkAllLower(self, word):
        for e in word:
            if not e.islower():
                return False
        return True
    
    def checkAllUpper(self, word):
        for e in word:
            if not e.isupper(): 
                return False
        return True
##################################################
def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        upper_case = word.upper()
        lower_case = word.lower()
        if upper_case == word:
            return True
        if lower_case == word:
            return True
        
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        return False
'''
