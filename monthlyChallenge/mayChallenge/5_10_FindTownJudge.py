# --------------------------------------------------------------------------
# Name:        Cousins in Binary Tree
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    In a town, there are N people labelled from 1 to N.  There is a rumor 
    that one of these people is secretly the town judge.

    If the town judge exists, then:
        1) The town judge trusts nobody.
        2) Everybody (except for the town judge) trusts the town judge.
        3) There is exactly one person that satisfies properties 1 and 2.
    
    You are given trust, an array of pairs trust[i] = [a, b] representing
    that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the 
    town judge.  Otherwise, return -1.
    
    Example 1:
        Input: N = 2, trust = [[1,2]]
        Output: 2
    
    Example 2:
        Input: N = 3, trust = [[1,3],[2,3]]
        Output: 3
    
    Example 3:
        Input: N = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1
        
    Example 4:
        Input: N = 3, trust = [[1,2],[2,3]]
        Output: -1
        
    Example 5:
        Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        Output: 3
    
    Note: 
        1) 1 <= N <= 1000
        2) trust.length <= 10000
        3) trust[i] are all different
        4) trust[i][0] != trust[i][1]
        5) 1 <= trust[i][0], trust[i][1] <= N
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_parent, x_depth = self.getParentNDepth(root, -1, 0, x)
        y_parent, y_depth = self.getParentNDepth(root, -1, 0, y)
        
        if x_parent != y_parent and x_depth == y_depth:
            return True
       
    def getParentNDepth(self, root, p, depth, target):
        if root: 
            # based case
            if root.val == target:
                return (p, depth)
            
            # Return level if Node is present in left subtree
            rl = self.getParentNDepth(root.left, root.val, depth+1, target)
            if rl:
                return rl
            
            # Else search in right subtree 
            return self.getParentNDepth(root.right, root.val, depth+1, target)
            
    
    










        
"""other faster methods (from other submissions)
##################################################
  def findJudge(self, N, trust):
      """
      :type N: int
      :type trust: List[List[int]]
      :rtype: int
      """
      if N == 1:
          return 1

      in_degrees = [0 for _ in range(N+1)]
      out_degrees = [0 for _ in range(N+1)]
      for a, b in trust:
          in_degrees[b] += 1
          out_degrees[a] += 1

      for i in range(1, N+1):
          if in_degrees[i] == N-1 and out_degrees[i] == 0:
              return i

      return -1
"""
