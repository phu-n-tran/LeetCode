# --------------------------------------------------------------------------
# Name:        Word Search 2
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a 2D board and a list of words from the dictionary, find all 
    words in the board.

    Each word must be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.

    Example:
    Input: 
        board = [
                  ['o','a','a','n'],
                  ['e','t','a','e'],
                  ['i','h','k','r'],
                  ['i','f','l','v']
                ]
        words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]

    Note:
        1. All inputs are consist of lowercase letters a-z.
        2. The values of words are distinct.
    source: https://www.youtube.com/watch?v=6EuYKlm2GkU
    https://leetcode.com/problems/word-search-ii/discuss/712733/Python-Trie-solution-with-dfs-explained
            
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            dic_to_search = root.children
            if symbol not in dic_to_search: 
                dic_to_search[symbol] = TrieNode()
            root.children = dic_to_search
            root = root.children[symbol]
        root.end_node = 1

class Solution:
    def findWords(self, board, words):
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words: trie.insert(word) 

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0: return

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return 
        tmp = board[i][j]
        if tmp not in node.children: return

        board[i][j] = "#"
        for x,y in [[0,-1], [0,1], [1,0], [-1,0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
        board[i][j] = tmp
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter]={}
                node = node[letter]
            node["#"]=word
        r = len(board)
        if r==0:
            return []
        c = len(board[0])
        matchWords =[]
        def get_words2(i,j,parent):
            letter = board[i][j]
            curNode = parent[letter]
            word_match = curNode.pop("#",False)
            if word_match:
                matchWords.append(word_match)
            board[i][j]="#"
            if i-1>=0 and board[i-1][j] in curNode:
                get_words2(i-1,j,curNode)
            if j-1>=0 and board[i][j-1] in curNode:
                get_words2(i,j-1,curNode)
            if i+1<r and board[i+1][j] in curNode:
                get_words2(i+1,j,curNode)
            if j+1<c and board[i][j+1] in curNode:
                get_words2(i,j+1,curNode)
            board[i][j]=letter
            if not curNode:
                parent.pop(letter)
        for i in xrange(r):
            for j in xrange(c):
                if board[i][j] in trie:
                    get_words2(i,j,trie)
        return matchWords
##################################################
def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(i,j,board,node):
            curr = board[i][j]
            board[i][j] = '*'
            trie = node[curr]
            if '#' in trie:
                res.append(trie['#'])
                trie.pop('#')
            if i > 0 and board[i-1][j] in trie:
                dfs(i-1,j,board,trie)
            if j > 0 and board[i][j-1] in trie:
                dfs(i,j-1,board,trie)
            if i < len(board)-1 and board[i+1][j] in trie:
                dfs(i+1,j,board,trie)
            if j < len(board[0])-1 and board[i][j+1] in trie:
                dfs(i,j+1,board,trie)
                
            board[i][j] = curr
                                
        root, res = {}, []
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    dfs(i,j,board,root)
        return res
'''
