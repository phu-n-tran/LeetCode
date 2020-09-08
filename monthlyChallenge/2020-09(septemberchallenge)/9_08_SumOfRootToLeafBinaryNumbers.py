# --------------------------------------------------------------------------
# Name:        Sum of Root To Leaf Binary Numbers
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary tree, each node has value 0 or 1.  Each root-to-leaf 
    path represents a binary number starting with the most significant bit.
    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could 
    represent 01101 in binary, which is 13.

    For all leaves in the tree, consider the numbers represented by the path
    from the root to that leaf.

    Return the sum of these numbers.

    Example 1:
      Input: [1,0,1,0,1,0,1]
      Output: 22
      Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

    Note:
      1. The number of nodes in the tree is between 1 and 1000.
      2. node.val is 0 or 1.
      3. The answer will not exceed 2^31 - 1.
      
    Hint:
      1. Find each path, then transform that path to an integer in base 10.
    https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solution/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(root, paths, binary):
            if root:   
                binary += str(root.val)
                preorder(root.left, paths, binary)
                preorder(root.right, paths, binary)
                
                if root.right is None and root.left is None:
                    paths.append("0b" + binary)
        
        if root is None:
            return 0
        
        paths = []
        preorder(root, paths, "")
        
        sumResult = 0
        for i in paths:
            sumResult += int(i,2)
            
        return sumResult
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return None
         
        if not root.left and not root.right:
            return root.val
        
        
        return self.evaluateSum(root, 0)
    
    def evaluateSum(self, root, total_sum):
        
        if not root.left and not root.right:
            return total_sum*2 + root.val
        
        elif not root.left:
            return self.evaluateSum( root.right, total_sum*2 + root.val )
            
        elif not root.right:
            return self.evaluateSum( root.left, total_sum*2 + root.val )
            
        else:
            return self.evaluateSum( root.right, total_sum*2 + root.val ) + \
                   self.evaluateSum( root.left, total_sum*2 + root.val )
##################################################
result = 0
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.countLeaf(root, 0)
        return self.result
        
    def countLeaf(self, node, current):
        if node == None:
            return
        val = current * 2 + node.val
        if node.left == None and node.right == None:
            self.result += val
            return
        self.countLeaf(node.left, val)
        self.countLeaf(node.right, val)
##################################################
def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.sum = 0
        
        def dfs(r, p):
            if r:
                p <<= 1
                p += r.val
                if not r.left and not r.right:
                    print(p, bin(p))
                    self.sum += p
                else:
                    dfs(r.left, p)
                    dfs(r.right, p)
        
        if not root:
            return 0
        
        dfs(root, 0)
        
        return self.sum
##################################################
def sumRootToLeaf(self, r):
        def f(r,v):
            if r:
                if not r.left and not r.right:
                    return v*2+r.val
                return f(r.left,v*2+r.val)+f(r.right,v*2+r.val)
            return 0
        return f(r,0)
##################################################
def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tot=0
        def traverse(root, start):
            if not root:
                return
            elif not root.left and not root.right:
                start = start+[root.val]
                self.tot+= int(''.join([str(i) for i in start]), base=2)
                return
            if root.left: traverse(root.left, start+[root.val])
            if root.right: traverse(root.right, start+[root.val])
            return
        
        traverse(root, [])
        return self.tot
'''
