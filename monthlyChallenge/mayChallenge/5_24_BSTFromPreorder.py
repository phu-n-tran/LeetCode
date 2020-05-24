# --------------------------------------------------------------------------
# Name:        Construct Binary Search Tree from Preorder Traversal
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Return the root node of a binary search tree that matches the given 
    preorder traversal.

    (Recall that a binary search tree is a binary tree where for every node,
    any descendant of node.left has a value < node.val, and any descendant of
    node.right has a value > node.val.  Also recall that a preorder traversal
    displays the value of the node first, then traverses node.left, then
    traverses node.right.)

    It's guaranteed that for the given test cases there is always possible
    to find a binary search tree with the given requirements.
    
    Example 1:
        Input: [8,5,1,7,10,12]
        Output: [8,5,10,1,7,null,12]
    
    Constraints: 
        1. 1 <= preorder.length <= 100
        2. 1 <= preorder[i] <= 10^8
        3. The values of preorder are distinct.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def builtBST(root, val):
            while True:
                if root.val < val:
                    if root.right:
                        root = root.right
                    else:
                        root.right = TreeNode(val)
                        return
                else:
                    if root.left:
                        root = root.left
                    else:
                        root.left = TreeNode(val)
                        return
        
        root = TreeNode(preorder.pop(0))
        
        for i in preorder:
            builtBST(root, i)
            
        return root

            
            
            
        
    










        
"""other faster methods (from other submissions)
##################################################
def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """    
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        st = [root]
        
        for i in range(1, len(preorder)):
            if preorder[i] <= st[-1].val:
                new_node = TreeNode(preorder[i])
                st[-1].left = new_node
                st.append(new_node)
            else:
                while(len(st)>0 and st[-1].val < preorder[i]):
                    last_node = st.pop()
                new_node = TreeNode(preorder[i])
                last_node.right = new_node
                st.append(new_node)
        return root
"""
