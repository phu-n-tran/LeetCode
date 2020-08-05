# --------------------------------------------------------------------------
# Name:        Add and Search Word - Data structure design
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string 
    containing only letters a-z or .. A . means it can represent any one letter.

    Example:
      addWord("bad")
      addWord("dad")
      addWord("mad")
      search("pad") -> false
      search("bad") -> true
      search(".ad") -> true
      search("b..") -> true
    
    Note:
      You may assume that all words are consist of lowercase letters a-z.
      
    Hint:
      You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordDict = defaultdict(set) 
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.wordDict[len(word)].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        import re
        
        if(word in self.wordDict[len(word)]):
            return True
        
        reObj = re.compile("^"+word+"$")

        for key in self.wordDict[len(word)]:
            if(reObj.match(key)):
                return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        n = len(word)
        self.map[n].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        w = self.map[n]
        if not w:
            return False
        if word in w:
            return True
        
        for i in range(n):
            if word[i] == '.':
                continue
            w = {x for x in w if x[i] == word[i]}
            
            if not w:
                return False
        return True
##################################################
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word:
            n = len(word)
            self.my_dict[n].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        n = len(word)
        if n not in self.my_dict:
            return False
        if "." not in word:
            return word in self.my_dict[n]
        
        for record in self.my_dict[n]:            
            for i, v in enumerate(word):
                if v != record[i] and v != ".":
                    break
            else:            
                return True
        return False
##################################################

'''
