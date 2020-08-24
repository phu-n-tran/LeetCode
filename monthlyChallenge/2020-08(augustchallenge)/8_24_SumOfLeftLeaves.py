# --------------------------------------------------------------------------
# Name:        Sum of Left Leaves
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Find the sum of all left leaves in a given binary tree.

    Example:

        3
       / \
      9  20
        /  \
       15   7

    There are two left leaves in the binary tree, with values 9 and 15 respectively. 
    Return 24.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorderHelper(root, prevDirection, count):
            if root:
                if root.left == None and root.right == None and prevDirection == "L":
                    count[0] += root.val
                
                inorderHelper(root.left, "L", count)
                inorderHelper(root.right, "R", count)
                
        count = [0]
        inorderHelper(root, "root", count)
        return count[0]
        
        
        
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       
        sum = 0
        if root is None:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            sum = root.left.val
        return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
##################################################
def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recusive(node):
            if not node:
                return 0
            if node.left:
                left_node = node.left
                if not left_node.left and not left_node.right:
                    self.ans += left_node.val

            recusive(node.left)
            recusive(node.right)
            
        self.ans = 0
        recusive(root)
        return self.ans
##################################################

'''
