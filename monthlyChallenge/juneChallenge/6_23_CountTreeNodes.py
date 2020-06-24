# --------------------------------------------------------------------------
# Name:        Count Complete Tree Nodes
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a complete binary tree, count the number of nodes.

    Note:
        1. Definition of a complete binary tree from Wikipedia:
           https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees
        2. In a complete binary tree every level, except possibly the last, 
           is completely filled, and all nodes in the last level are as far
           left as possible. It can have between 1 and 2h nodes inclusive at 
           the last level h.

    Example:
        Input: 
              1
             / \
            2   3
           / \  /
          4  5 6
          
        Output: 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.size = 0
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):    
            if root:
                self.size += 1
                helper(root.left)
                helper(root.right)
        
        self.size = 0
        helper(root)
        return self.size
        
        
        
        
        
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == right:
            return 2 ** left + self.countNodes(root.right)
        else:
            return 2 ** right + self.countNodes(root.left)
        
        
    def helper(self, root):
        if root is None:
            return 0
        return 1 + self.helper(root.left)
#################################################
def height(self, root):
        h = 0
        while root:
            h+=1
            root=root.left
        return h 
    
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if lh==rh:
            return pow(2, lh) + self.countNodes(root.right)
        else:
            return pow(2, rh) + self.countNodes(root.left)
#################################################
def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lh = rh = 0
        left = right = root
        while left != None:
            left = left.left
            lh += 1
        while right != None:
            right = right.right
            rh += 1
        if lh == rh:
            return 2 ** lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
'''
