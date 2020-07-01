# --------------------------------------------------------------------------
# Name:        Implement Trie (Prefix Tree)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Implement a trie with insert, search, and startsWith methods.
    
    Example:
        Trie trie = new Trie();

        trie.insert("apple");
        trie.search("apple");   // returns true
        trie.search("app");     // returns false
        trie.startsWith("app"); // returns true
        trie.insert("app");   
        trie.search("app");     // returns true
    
    Note: 
        1) You may assume that all inputs are consist of lowercase letters a-z.
        2) All inputs are guaranteed to be non-empty strings.
"""

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trieTree = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.trieTree
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        root["found"] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.trieTree
        for letter in word:
            if letter not in root:
                return False
            root = root[letter]
        return root.get("found", False)
            
            
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.trieTree
        for letter in prefix:
            if letter not in root:
                return False
            root = root[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        
        
        
        
        
"""other faster methods (from other submissions)
##################################################
   
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for w in word: 
            if w not in t: 
                return False
            t = t[w]
        return '#' in t:
"""
