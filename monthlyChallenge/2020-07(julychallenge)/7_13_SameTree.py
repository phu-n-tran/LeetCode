# --------------------------------------------------------------------------
# Name:        Same Tree
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two binary trees, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical
    and the nodes have the same value.

    Example 1:
      Input:   
                 1         1
                / \       / \
               2   3     2   3

              [1,2,3],   [1,2,3]

      Output: true
      
    Example 2:
      Input:
                 1         1
                /           \
               2             2

              [1,2],     [1,null,2]

      Output: false
      
    Example 3:
      Input:  
                 1         1
                / \       / \
               2   1     1   2

              [1,2,1],   [1,1,2]

      Output: false
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def inOrder(p, q, result):
            if p is not None and q is None:
                result[0] = False
            if p is None and q is not None:
                result[0] = False
            if p and q:
                if p.val != q.val:
                    result[0] = False
                inOrder(p.left, q.left, result)
                inOrder(p.right, q.right, result)
        
        result = [True]
        inOrder(p, q, result)
        return result[0]
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        resp=[]
        self.traverseTree(p,q,resp)
        for r in resp:
            if not r:
                return False
        return True
        
    
    def traverseTree(self,p,q,response):
        if p is None and q is None:
            response.append(True)
        if p is not None and q is None:
            response.append(False)
        if p is None and q is not None:
            response.append(False)
        if p is not None and q is not None and p.val==q.val:
            self.traverseTree(p.left,q.left,response)
            self.traverseTree(p.right,q.right,response)
        if p is not None and q is not None and p.val!=q.val:
            response.append(False)
##################################################
def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q :
            return False
        
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
##################################################

'''
