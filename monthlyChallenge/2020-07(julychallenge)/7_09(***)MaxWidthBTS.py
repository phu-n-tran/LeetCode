# --------------------------------------------------------------------------
# Name:        Maximum Width of Binary Tree
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary tree, write a function to get the maximum width of the 
    given tree. The width of a tree is the maximum width among all levels. 
    The binary tree has the same structure as a full binary tree, but some
    nodes are null.
  
    The width of one level is defined as the length between the end-nodes 
    (the leftmost and right most non-null nodes in the level, where the null
    nodes between the end-nodes are also counted into the length calculation.

    Example 1:
      Input: 
                 1
               /   \
              3     2
             / \     \  
            5   3     9 
      Output: 4
      Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
    
    Example 2:
      Input: 

                1
               /  
              3    
             / \       
            5   3     

      Output: 2
      Explanation: The maximum width existing in the third level with the length 2 (5,3).
    
    Example 3:
      Input: 

                1
               / \
              3   2 
             /        
            5      
      Output: 2
      Explanation: The maximum width existing in the second level with the length 2 (3,2).
   
    Example 4:
      Input: 

                1
               / \
              3   2
             /     \  
            5       9 
           /         \
          6           7
      Output: 8
      Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

    Note: Answer will in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level_old, num_old, max_width = 1, 1, 0
        queue = deque([[level_old,num_old,root]])

        while queue:    
            [num, level, node] = queue.popleft()
            if level > level_old:
                level_old, num_old = level, num
                
            max_width = max(max_width, num - num_old + 1)
            if node.left:  queue.append([num*2,  level+1, node.left])
            if node.right: queue.append([num*2+1,level+1, node.right])
                
        return max_width
        
        
        
        
                
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def widthOfBinaryTree(self, root):
        if not root: 
            return []
        
        width = 0
        level = [(root, 1)]
        
        # Keep going untill current level has some nodes.
        while level:
            # Put all children of current level in next_level.
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            
            for item, num in level:
                if item.left:   # Make sure to not put the Null nodes
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2+1))
            level = next_level
            
        return width
##################################################
def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.right is None and root.left is None:
            return 1
        coord = {root: 0}
        node = [root]
        z = 1
        d = 1
        while z > 0:
            coord_new = {}
            node_new = []
            for n in node:
                if n.left is not None:
                    coord_new[n.left] = 2 * coord[n]
                    node_new.append(n.left)
                if n.right is not None:
                    coord_new[n.right] = 2 * coord[n] + 1
                    node_new.append(n.right)
            z = len(coord_new)
            if z > 1:
                d = max(d, coord_new[node_new[-1]] - coord_new[node_new[0]] + 1)
            coord = coord_new
            node = node_new
        return d
##################################################
def widthOfBinaryTree(self, root):
        ans = 0
        level = [(root, 0)]
        while level:
          new_level = []
          ans = max(ans, level[-1][1] - level[0][1] + 1)
          for node, pos in level:
            if node.left:
              new_level.append((node.left, pos * 2))
            if node.right:
              new_level.append((node.right, pos * 2 + 1))
              
          level = new_level
        return ans
        
'''
