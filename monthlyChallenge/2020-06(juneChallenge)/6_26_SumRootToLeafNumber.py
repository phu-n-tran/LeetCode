
# --------------------------------------------------------------------------
# Name:        Sum Root to Leaf Numbers
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers.

    Note: A leaf is a node with no children.

    Example:
      Input: [1,2,3]
          1
         / \
        2   3
      Output: 25
      Explanation:
        The root-to-leaf path 1->2 represents the number 12.
        The root-to-leaf path 1->3 represents the number 13.
        Therefore, sum = 12 + 13 = 25.
   
    Example 2:
      Input: [4,9,0,5,1]
          4
         / \
        9   0
       / \
      5   1
      Output: 1026
      Explanation:
        The root-to-leaf path 4->9->5 represents the number 495.
        The root-to-leaf path 4->9->1 represents the number 491.
        The root-to-leaf path 4->0 represents the number 40.
        Therefore, sum = 495 + 491 + 40 = 1026.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def InOrderhelper(root, pathNum, myList):
            # in case there is 0, 1 or 2 element(s) in the BST 
            if root is None:
                return
            
            if root.right is None and root.left is None:
                # pathNum will accumlate the path from root to a specific leave
                # store in a list which is pass by reference while pathNum
                # to test
                # print(pathNum + str(root.val))
                myList.append(int(pathNum + str(root.val)))
                return
            
            InOrderhelper(root.left, pathNum + str(root.val), myList)
            InOrderhelper(root.right, pathNum + str(root.val), myList)
        
        
        pathNum = ""
        myList = []
        
        InOrderhelper(root, pathNum, myList)
        return sum(myList)
        
        
        
        
        
        
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_to_leaf = 0
        stack = [(root, 0) ]
        
        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
                        
        return root_to_leaf
#################################################
def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root,s,res):
            if root and not root.left and not root.right:
                res.append(s)
                return
            if root.left:
                helper(root.left,((s*10)+root.left.val),res)
            if root.right:
                helper(root.right,((s*10)+root.right.val),res)
        
        
            return
        if not root: 
            return 0
        res = []
        helper(root,root.val,res)
        print(res)
        return sum(res)
#################################################
'''
