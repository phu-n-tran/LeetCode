# --------------------------------------------------------------------------
# Name:        Stream of Characters
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    mplement the StreamChecker class as follows:
      - StreamChecker(words): Constructor, init the data structure with the 
                            given words.
                            
      - query(letter): returns true if and only if for some k >= 1, the last k
                     characters queried (in order from oldest to newest, 
                     including this letter just queried) spell one of the 
                     words in the given list.


    Example:
      StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
      streamChecker.query('a');          // return false
      streamChecker.query('b');          // return false
      streamChecker.query('c');          // return false
      streamChecker.query('d');          // return true, because 'cd' is in the wordlist
      streamChecker.query('e');          // return false
      streamChecker.query('f');          // return true, because 'f' is in the wordlist
      streamChecker.query('g');          // return false
      streamChecker.query('h');          // return false
      streamChecker.query('i');          // return false
      streamChecker.query('j');          // return false
      streamChecker.query('k');          // return false
      streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 
    Note:
      1. 1 <= words.length <= 2000
      2. 1 <= words[i].length <= 2000
      3. Words will only consist of lowercase English letters.
      4. Queries will only consist of lowercase English letters.
      5. The number of queries is at most 40000.
"""


class TrieNode:
    def __init__(self):
        self.nxt = collections.defaultdict(TrieNode)
        self.word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.nxt[char]
        node.word = True
        
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1]) 
            
        self.stream = collections.deque([])
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)
        
        node = self.trie.root # only one start point
        for char in self.stream:
            if not char in node.nxt:
                return False
            node = node.nxt[char]
            if node.word:
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.stream = collections.deque([])
        self.root = {}
        for word in set(words):
            curNode = self.root
            for ch in word[::-1]:
                if ch not in curNode:
                    curNode[ch] = {}
                curNode = curNode[ch]
            curNode['#'] = word

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)
        curNode = self.root
        for ch in self.stream:
            if '#' in curNode:
                return True
            if ch not in curNode:
                return False
            curNode = curNode[ch]
        return '#' in curNode
##################################################
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # reverse Trie
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie       
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node
##################################################

'''
