# --------------------------------------------------------------------------
# Name:        All Elements in Two Binary Search Trees
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two binary search trees root1 and root2.

    Return a list containing all the integers from both trees sorted in ascending order.

    Example 1:
      Input: root1 = [2,1,4], root2 = [1,0,3]
      Output: [0,1,1,2,3,4]
    
    Example 2:
      Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
      Output: [-10,0,0,1,2,5,7,10]
    
    Example 3:
      Input: root1 = [], root2 = [5,1,7,0,2]
      Output: [0,1,2,5,7]
    
    Example 4:
      Input: root1 = [0,-10,10], root2 = []
      Output: [-10,0,10]
    
    Example 5:
      Input: root1 = [1,null,8], root2 = [8,1]
      Output: [1,1,8,8]
 

    Constraints:
      1. Each tree has at most 5000 nodes.
      2. Each node's value is between [-10^5, 10^5].
      
    Hints:
      1. Traverse the first tree in list1 and the second tree in list2.
      2. Merge the two trees in one list and sort it.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inOrder(root, result):
            if root:
                inOrder(root.left, result)
                result.append(root.val)
                inOrder(root.right, result)
        
        result = []
        
        inOrder(root1, result)
        inOrder(root2, result)
        
        return sorted(result)
                
                
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        stack1,stack2,output = [],[],[]
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right
        return output
##################################################
def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(root):
            ret=[]
            stack=[]
            while root or stack:
                while root:
                    stack.append(root)
                    root=root.left
                cur=stack.pop()
                ret.append(cur.val)
                if cur.right: root=cur.right
            return ret
        
        nums1=inorder(root1)
        nums2=inorder(root2)
        
        return sorted(nums1+nums2)
##################################################
def getAllElements(self, root1, root2):
        out = []
        def traverse(node):
            if node:
                out.append(node.val)
                traverse(node.left)
                traverse(node.right)
        traverse(root1)
        traverse(root2)
        return sorted(out)
##################################################
'''
