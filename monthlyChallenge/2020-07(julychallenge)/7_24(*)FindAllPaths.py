# --------------------------------------------------------------------------
# Name:        All Paths From Source to Target
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a directed, acyclic graph of N nodes.  Find all possible paths
    from node 0 to node N-1, and return them in any order.

    The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
    graph[i] is a list of all nodes j for which the edge (i, j) exists.

    Example:
      Input: [[1,2], [3], [3], []] 
      Output: [[0,1,3],[0,2,3]] 
      Explanation: The graph looks like this:
      0--->1
      |    |
      v    v
      2--->3
      There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    
    Note:
      1. The number of nodes in the graph will be in the range [2, 15].
      2. You can print different paths in any order, but you should keep the order of nodes inside one path.
"""


#### DFS APPROACH ####
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(graph, source, destination, curPath, result):
            # if soruce reached destination add that path in result
            if source == destination:
                result.append(curPath)
            
            # add current vertex
            curPath.append(source)
            for vertex in graph[source]:
                newList = curPath[:]
                dfs(graph, vertex, destination, newList, result)
                
       
        result = []
        dfs(graph, 0, len(graph)-1, [], result)
        return result

#### BFS APPROACH ####
# class Solution(object):
#     def allPathsSourceTarget(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         result = []
#         queue = [[0]]
#         destination = len(graph)-1
        
#         while queue:
#             curPath = queue.pop(0)
            
#             if curPath[-1] == destination:
#                 result.append(curPath)
#             else:
#                 for neighbor in graph[curPath[-1]]:
#                     queue.append(curPath + [neighbor])
        
#         return result
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans, end = [],  len(graph) - 1
        def dfs(node, path):
            if node == end:
                ans.append(path)
                return
            
            for child in graph[node]:
                dfs(child, path + [child])    
        
        dfs(0, [0])
        return ans
##################################################
def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(cur, path):
            if cur == len(graph) - 1: 
                res.append(path)
            else:
                for i in graph[cur]: 
                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
##################################################
def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph:
            return []
        dict=defaultdict(list)
        for i,each in enumerate(graph):
            for each in each:
                dict[i].append(each)
        #print(dict)
        
        q=collections.deque([])
        for each in graph[0]:
            q.append([0,each])
        #print(q)
        dest=len(graph)-1
        l=[]
        while q:
            node=q.popleft()
            if node[-1]==dest:
                l.append(node)
            else:
                for each in dict[node[-1]]:
                    v=node+[each]
                    q.append(v)
        return l
'''
