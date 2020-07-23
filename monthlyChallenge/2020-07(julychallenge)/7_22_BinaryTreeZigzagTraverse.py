# --------------------------------------------------------------------------
# Name:        Binary Tree Zigzag Level Order Traversal
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary tree, return the zigzag level order traversal of its 
    nodes' values. (ie, from left to right, then right to left for the 
    next level and alternate between).

    For example:
      Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
      return its zigzag level order traversal as:
        [
          [3],
          [20,9],
          [15,7]
        ]
      explain: 1st level: left to right
               2nd level: right to left
               3rd level: left to right
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def inOrder(root, depth, result):
            if root:
                if len(result) <= depth:
                    result.append([])
                
                # if depth is even: store from left to right - append at the end
                if depth%2 == 0: 
                    result[depth].append(root.val)
                else: # if depth is odd: store from right to left - append at the front
                    result[depth].insert(0, root.val)
                
                inOrder(root.left, depth+1, result)
                inOrder(root.right, depth+1, result)
        
        result = []
        if root:
            inOrder(root, 0, result)
        
        return result
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
#         level = 0
#         #global
#         res = []
#         def rec(node, currlevel):
#             if not node:
#                 return
#             if currlevel == len(res):
#                 res.append([])
#             if currlevel % 2 == 0:
#                 rec(node.right,currlevel+1)
#                 rec(node.left, currlevel+1)
#             else:
#                 rec(node.left,currlevel+1)
#                 rec(node.right, currlevel+1)
#             res[currlevel].append(node.val)
                
#         rec(root,level)   
#         return res
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in xrange(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res
##################################################
def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [(root, 0)]
        values = []
        while stack:
            tmp, i = stack.pop(0)
            if not tmp:
                continue
                
            if len(values) == i:
                values.append([])
            
            if i %2 == 0:
                values[i].append(tmp.val)
            else:
                values[i].insert(0, tmp.val)
                
            stack.append((tmp.left, i+1))
            stack.append((tmp.right, i+1))
                
        return values
##################################################
def recur(self, node, level, rtn):
        if not node:
            return 
        if len(rtn) < level:
            rtn.append([])
        rtn[level-1].append(node.val)
        self.recur(node.left, level + 1, rtn)
        self.recur(node.right, level + 1, rtn)
    
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        self.recur(root,1,levels)
        for index in range(len(levels)):
            if index % 2 == 1:
                levels[index] = levels[index][::-1]
        return levels
'''
