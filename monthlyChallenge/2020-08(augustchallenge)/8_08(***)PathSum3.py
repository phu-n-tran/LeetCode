# --------------------------------------------------------------------------
# Name:        Path Sum III
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given a binary tree in which each node contains an integer value.

    Find the number of paths that sum to a given value.

    The path does not need to start or end at the root or a leaf, but it 
    must go downwards (traveling only from parent nodes to child nodes).

    The tree has no more than 1,000 nodes and the values are in the 
    range -1,000,000 to 1,000,000.

    Example:
      root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

            10
           /  \
          5   -3
         / \    \
        3   2   11
       / \   \
      3  -2   1

      Return 3. The paths that sum to 8 are:
        1.  5 -> 3
        2.  5 -> 2 -> 1
        3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        from collections import defaultdict
        sum_map = defaultdict(int)
        sum_map[0] = 1
        return self.findPathSum(root, sum_map, 0, sum)

    def findPathSum(self, node, sum_map, cur_sum, target):
        if not node:
            return 0
        cur_sum += node.val
        ans = sum_map[cur_sum - target]
        sum_map[cur_sum] += 1
        ans += self.findPathSum(node.left, sum_map, cur_sum, target) + \
            self.findPathSum(node.right, sum_map, cur_sum, target)
        sum_map[cur_sum] -= 1
        return ans
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def pathSum(self, root, sum):
        running_sum_counter = defaultdict(int)
        # This step is important; otherwise we will miss paths
        # from the root
        running_sum_counter[0] = 1       
        return dfs(root, 0, running_sum_counter, sum)
    
def dfs(root, running_sum, running_sum_counter, target):
            if not root:
                return 0
            # Update running sum and counter
            # This is the trick to make it O(N) fast:
            # In each array, we need to look for continuous subarrays
            # that sum up to the target sum. To remove duplicate sums,
            # we keep a running sum at each index, so that when the array
            # is extended, to check how many subarrays would sum up to
            # the target, we just check the count of:
            # new_running_sum - target = # existing running sums
            # Think of it as this:
            # |--prevSum---|-----target-----|
            # |------newRunningSum----------|
            # target = newRunningSum - prevSum, and prevSum can be cached
            # so we compute each sum only once.
            running_sum += root.val
            num_paths = running_sum_counter[running_sum - target]
            running_sum_counter[running_sum] += 1
            
            # Go down
            num_paths += dfs(root.left, running_sum, running_sum_counter, target)
            num_paths += dfs(root.right, running_sum, running_sum_counter, target)
            
            # Before return, revert the "damage" -- we'll be back
            # to a state where the updated running_sum hasn't
            # been encountered yet
            running_sum_counter[running_sum] -= 1
            return num_paths
##################################################
class Solution(object):
    def __init__(self):
        self.count = 0
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        mem = defaultdict(int)
        mem[0] = 1
        self.pathCount(root, 0, sum, mem)
        return self.count
        
    def pathCount(self, node, curSum, sum, mem):
        if not node:
            return
        curSum += node.val
        self.count += mem[curSum - sum]
        mem[curSum] += 1
        self.pathCount(node.left, curSum, sum, mem)
        self.pathCount(node.right, curSum, sum, mem)
        mem[curSum] -= 1
##################################################
def pathSum(self, root, k):
        def preorder(node, curr_sum):
            if not node:
                return 
            
            curr_sum += node.val
            
            if curr_sum == k:
                self.count += 1
            
            self.count += h[curr_sum - k]
            
            h[curr_sum] += 1
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            h[curr_sum] -= 1
            
        self.count= 0
        h = defaultdict(int)
        preorder(root, 0)
        return self.count
'''
