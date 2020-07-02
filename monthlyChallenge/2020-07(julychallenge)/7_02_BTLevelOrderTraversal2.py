# --------------------------------------------------------------------------
# Name:        Arranging Coins
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary tree, return the bottom-up level order traversal of its 
    nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:
      Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
      return its bottom-up level order traversal as:
        [
          [15,7],
          [9,20],
          [3]
        ]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bottomUp(root, result, level):
            if root:
                
                if len(result) <= level:
                    result.append([])
                result[level] += [root.val]
                
                bottomUp(root.left, result, level+1)
                bottomUp(root.right, result, level+1)
        
        result = []
        bottomUp(root, result, 0)
        return result[::-1]
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def levelOrderBottom(self, root):
        if not root:
            return []

        prev = [root]
        ret = []
        while prev:
            ret.append([n.val for n in prev])
            curr = []
            for node in prev:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            prev = curr
        return list(reversed(ret))
##################################################
def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [root]
        level=0
        while queue: 
            node = [nod for nod in queue]         
            temp =[]
            res.append([nod.val for nod in node])
            for nod in node:
                if nod.left:
                    temp.append(nod.left)
                if nod.right:
                    temp.append(nod.right)
            queue = temp
            level+=1
            
        return res[::-1]
##################################################

'''
