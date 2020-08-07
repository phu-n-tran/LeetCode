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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        nodes_list = []
        
        def dfs(node, row, col):
            
            if not node:
                return
            
            dfs(node.left, row+1, col-1)
            
            nodes_list.append((col, row, node.val))
                
            dfs(node.right, row+1, col+1)
            
        
        dfs(root, 0, 0)
         # sorting a tuple: first sorts by element 0, then by element 1, then by element 2
        nodes_list.sort()
        
        ans  = OrderedDict()
        
        for tup in nodes_list:
            
            if tup[0] not in ans:
                
                ans[tup[0]] = [tup[2]]
            else:
            
                ans[tup[0]].append(tup[2])
            
        return ans.values()
##################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import defaultdict, deque
    
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        store = defaultdict(list)
        q = deque([(0,root,0),])
        mind, maxd = 0,0
        while q:            
            r,node,d = q.pop()
            mind = min(mind,d)
            maxd = max(maxd,d)
            store[d].append((r,node.val))                
            if node.left:
                q.appendleft((r+1,node.left,d-1))
            if node.right:
                q.appendleft((r+1,node.right,d+1))
        ans = []
        for x in range(mind,maxd+1):
            ans.append([val for row,val in sorted(store[x])])

        return ans
##################################################

'''
