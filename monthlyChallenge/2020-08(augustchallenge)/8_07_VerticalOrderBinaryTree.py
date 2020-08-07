# --------------------------------------------------------------------------
# Name:        Vertical Order Traversal of a Binary Tree
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a binary tree, return the vertical order traversal of its nodes values.

    For each node at position (X, Y), its left and right children respectively 
    will be at positions (X-1, Y-1) and (X+1, Y-1).

    Running a vertical line from X = -infinity to X = +infinity, whenever the 
    vertical line touches some nodes, we report the values of the nodes in order
    from top to bottom (decreasing Y coordinates).

    If two nodes have the same position, then the value of the node that is 
    reported first is the value that is smaller.

    Return an list of non-empty reports in order of X coordinate. 
    Every report will have a list of values of nodes.

 
    Example 1:
        Input: [3,9,20,null,null,15,7]
        Output: [[9],[3,15],[20],[7]]
        Explanation: 
            Without loss of generality, we can assume the root node is at position (0, 0):
            Then, the node with value 9 occurs at position (-1, -1);
            The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
            The node with value 20 occurs at position (1, -1);
            The node with value 7 occurs at position (2, -2).

    Example 2:
        Input: [1,2,3,4,5,6,7]
        Output: [[4],[2],[1,5,6],[3],[7]]
        Explanation: 
        The node with value 5 and the node with value 6 have the same position according to the given scheme.
        However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 
    Note:
        1. The tree will have between 1 and 1000 nodes.
        2. Each node's value will be between 0 and 1000.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def inOrderTracking(root, x_pos, y_pos, result):
            if root:
                # key will be x position, value will be tuple (value, y_pos)
                # note: use y_pos to keep track of the order
                result[x_pos] = result.get(x_pos, []) + [(root.val, y_pos)]
                inOrderTracking(root.left, x_pos-1, y_pos-1, result)
                inOrderTracking(root.right, x_pos+1, y_pos-1, result)
                
        result = dict()
        inOrderTracking(root, 0, 0, result)
        # print(result)
        
        finalList = []
        for i in sorted(result):
            # first sort the tuple in list of each key, (2nd ele by descending, 1st ele by ascending)
            # then get rid of the tuple and only keep the 1st ele (value)
            # finally append it in order
            finalList.append([ele[0] for ele in sorted(result[i], key=lambda x: (x[1], -x[0]), reverse=True)])
        
        return finalList
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        nodes_list = []
        
        def dfs(node, row, col):
            
            if not node:
                return
            
            dfs(node.left, row+1, col-1)
            
            nodes_list.append((col, row, node.val))
                
            dfs(node.right, row+1, col+1)
            
        
        dfs(root, 0, 0)
         # sorting a tuple: first sorts by element 0, then by element 1, then by element 2
        nodes_list.sort()
        
        ans  = OrderedDict()
        
        for tup in nodes_list:
            
            if tup[0] not in ans:
                
                ans[tup[0]] = [tup[2]]
            else:
            
                ans[tup[0]].append(tup[2])
            
        return ans.values()
##################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import defaultdict, deque
    
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        store = defaultdict(list)
        q = deque([(0,root,0),])
        mind, maxd = 0,0
        while q:            
            r,node,d = q.pop()
            mind = min(mind,d)
            maxd = max(maxd,d)
            store[d].append((r,node.val))                
            if node.left:
                q.appendleft((r+1,node.left,d-1))
            if node.right:
                q.appendleft((r+1,node.right,d+1))
        ans = []
        for x in range(mind,maxd+1):
            ans.append([val for row,val in sorted(store[x])])

        return ans
##################################################

'''
