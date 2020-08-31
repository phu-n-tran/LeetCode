# --------------------------------------------------------------------------
# Name:        Delete Node in a BST
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a root node reference of a BST and a key, delete the node with the
    given key in the BST. Return the root node reference (possibly updated)
    of the BST.

    Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.
    Note: Time complexity should be O(height of tree).

    Example:
      root = [5,3,6,2,4,null,7]
      key = 3

            5
           / \
          3   6
         / \   \
        2   4   7

      Given key to delete is 3. So we find the node with value 3 and delete it.

      One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

            5
           / \
          4   6
         /     \
        2       7

      Another valid answer is [5,2,6,null,4,null,7].

            5
           / \
          2   6
           \   \
            4   7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        # Find node
        if key < root.val : # if less
            root.left = self.deleteNode(root.left,key)
        elif key > root.val :# if greater
            root.right = self.deleteNode(root.right,key)  
        else: # Node to delete
            # Case 1: No childs.
            if root.left == None and root.right == None:
                root = None
                
            # Case 2: One child
            elif root.left == None and root.right != None :
                root = root.right
            elif root.right == None and root.left != None :
                root = root.left
                
            # Case 3: 2 children
            else:
                minRoot = self.findMinNode(root.right)
                root.val = minRoot.val
                root.right = self.deleteNode(root.right,root.val) # now delete the min node
                
        return root

    def findMinNode(self, root):
        current = root 
  
        # loop down to find the lefmost leaf 
        while(current.left is not None): 
            current = current.left 

        return current
                
        
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        
        # we always want to delete the node when it is the root of a subtree,
        # so we handle left or right according to the val.
        # if the node does not exist, we will hit the very first if statement and return None.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # now the key is the root of a subtree
        else:
            # if the subtree does not have a left child, we just return its right child
            # to its father, and they will be connected on the higher level recursion.
            if not root.left:
                return root.right
            
            # if it has a left child, we want to find the max val on the left subtree to 
            # replace the node we want to delete.
            else:
                # try to find the max value on the left subtree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                    
                # replace
                root.val = tmp.val
                
                # since we have replaced the node we want to delete with the tmp, now we don't
                # want to keep the tmp on this tree, so we just use our function to delete it.
                # pass the val of tmp to the left subtree and repeat the whole approach.
                root.left = self.deleteNode(root.left, tmp.val)
        
        return root
##################################################
def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        # This is it
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Two children
        leftChild = root.left
        while leftChild.right:
            leftChild = leftChild.right
        root.val = leftChild.val
        root.left = self.deleteNode(root.left, root.val)
        return root
##################################################

'''
