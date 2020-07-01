# --------------------------------------------------------------------------
# Name:        Invert a Binary Tree
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Invert a binary tree.

    Example:
        Input: [4,2,7,1,3,6,9]

               4
             /   \
            2     7
           / \   / \
          1   3 6   9

        Output: [4,7,2,9,6,3,1]
               4
             /   \
            7     2
           / \   / \
          9   6 3   1

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root, invertRoot, direction):
            if root:
                if direction == 'r':
                    # create the node first then move to that node instead of passing it in the arg as func call
                    invertRoot.right = TreeNode(root.val)
                    invertRoot = invertRoot.right
                elif direction == 'l':
                    invertRoot.left = TreeNode(root.val)
                    invertRoot = invertRoot.left
                    
                # the third arg use to keep track of the inverse direction
                helper(root.left, invertRoot, 'r')
                helper(root.right, invertRoot, 'l')
        
        invertRoot = None
        if root:
            invertRoot = TreeNode(root.val)
            helper(root, invertRoot, 'c')
        return invertRoot
 



        
'''other faster methods (from other submissions)
##################################################
def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        left, right = root.left, root.right
        
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        
        return root
'''
