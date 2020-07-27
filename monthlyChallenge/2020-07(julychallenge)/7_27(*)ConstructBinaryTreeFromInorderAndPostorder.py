# --------------------------------------------------------------------------
# Name:        Construct Binary Tree from Inorder and Postorder Traversal
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note:
      You may assume that duplicates do not exist in the tree.

    For example, given
      inorder = [9,3,15,20,7]
      postorder = [9,15,7,20,3]
      Return the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return
        
        # last element in the postorder is the top (parent) node of all node in front of it
        root = TreeNode(postorder[-1])
        # anything in front of parent node is it left children in inorder array and other is it right children
        border_idx = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:border_idx], postorder[:border_idx])
        root.right = self.buildTree(inorder[border_idx+1:], postorder[border_idx:-1])
        
        return root
        
        
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)
##################################################
def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        index_map = {v: i for i, v in enumerate(inorder)}
        
        def construct(left, right):
            if left > right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            index = index_map[val]
            
            # Right first because _postorder_
            root.right = construct(index + 1, right)
            root.left = construct(left, index - 1)
            
            return root
        
        return construct(0, len(inorder) - 1)
##################################################
def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        def helper(left, right):
            if left>right: return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            index = d[val]
            
            
            root.right = helper(index+1,right)
            root.left = helper(left,index-1)
            
            return root
'''
