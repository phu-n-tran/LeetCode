# --------------------------------------------------------------------------
# Name:        Cousins in Binary Tree
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    In a binary tree, the root node is at depth 0, and children of each 
    depth k node are at depth k+1.

    Two nodes of a binary tree are cousins if they have the same depth, 
    but have different parents.

    We are given the root of a binary tree with unique values, and the 
    values x and y of two different nodes in the tree.

    Return true if and only if the nodes corresponding to the values x and 
    y are cousins.
    
    Example 1:
        Input: root = [1,2,3,4], x = 4, y = 3
        Output: false
    
    Example 2:
        Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
        Output: true
    
    Example 3:
        Input: root = [1,2,3,null,4], x = 2, y = 3
        Output: false
    
    Note: 
        1. The number of nodes in the tree will be between 2 and 100.
        2. Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_parent, x_depth = self.getParentNDepth(root, -1, 0, x)
        y_parent, y_depth = self.getParentNDepth(root, -1, 0, y)
        
        if x_parent != y_parent and x_depth == y_depth:
            return True
       
    def getParentNDepth(self, root, p, depth, target):
        if root: 
            # based case
            if root.val == target:
                return (p, depth)
            
            # Return level if Node is present in left subtree
            rl = self.getParentNDepth(root.left, root.val, depth+1, target)
            if rl:
                return rl
            
            # Else search in right subtree 
            return self.getParentNDepth(root.right, root.val, depth+1, target)
            
    
    










        
"""other faster methods (from other submissions)
##################################################
def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def dfs(root,x,p,d,res):
            if not root:
                return 
            if root.val==x:
                res[0]=p
                res[1]=d
                return 
            dfs(root.left,x,root,d+1,res)
            dfs(root.right,x,root,d+1,res)
            
            
        node1=[None,0]
        node2=[None,0]
        dfs(root,x,None,0,node1)
        dfs(root,y,None,0,node2)
        
        if node1[0]!=node2[0] and node1[1]==node2[1]:
            return True
        return False
"""
