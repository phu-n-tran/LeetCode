# --------------------------------------------------------------------------
# Name:        Course Schedule (graph approach)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    There are a total of numCourses courses you have to take, labeled 
    from 0 to numCourses-1.

    Some courses may have prerequisites, for example to take course 0 you 
    have to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is 
    it possible for you to finish all courses?
    
    Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take. 
                     To take course 1 you should have finished course 0.
                     So it is possible.
 
    Example 2:
        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take. 
                     To take course 1 you should have finished course 0, 
                     and to take course 0 you should also have finished 
                     course 1. So it is impossible.
    
    Constraints: 
        1. The input prerequisites is a graph represented by a list of edges, 
           not adjacency matrices. Read more about how a graph is represented.
           https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
        2. You may assume that there are no duplicate edges in the input prerequisites.
        3. 1 <= numCourses <= 10^5
        
    Hint:
        1. This problem is equivalent to finding if a cycle exists in a 
           directed graph. If a cycle exists, no topological ordering 
           exists and therefore it will be impossible to take all courses.
        2. Topological Sort via DFS - A great video tutorial (21 minutes) on 
           Coursera explaining the basic concepts of Topological Sort.
        3. Topological sort could also be done via BFS.
           https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def hasCycle(graph, visited, stack, v):
            visited[v] = True
            stack[v] = True
            
            for adj_v in graph[v]:
                print(adj_v)
                if stack[adj_v]:
                    return True
                if not visited[adj_v]:
                    if hasCycle(graph, visited, stack, adj_v):
                        return True
                
            stack[v] = False
            return False
            
        
        graph = defaultdict(list)
        
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [False] * (numCourses)
        stack = [False] * (numCourses)
        
        # for v in range(numCourses): 
        for v in graph.keys(): # b/c this is defaultdict 
            if not visited[v]:
                if hasCycle(graph, visited, stack, v):
                    return False
        return True
    
    
        
        
          
            
        
 



        
"""other faster methods (from other submissions)
##################################################
def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        def dfs(i):
            # loop found, -1 = node being visited.
            if visited[i] == -1:
                return False
            if visited[i] == 1: #already visited
                return True
            
            visited[i] = -1
            
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
########################################################
def canFinish(self, numCourses, prerequisites):
        self.adj_dict = defaultdict(set)
        for i, j in prerequisites:
            self.adj_dict[i].add(j)

        self.Visited = [0] * numCourses
        self.FoundCycle = 0

        for i in range(numCourses):
            if self.FoundCycle == 1: break   # early stop if the loop is found
            if self.Visited[i] == 0:
                self.DFS(i)

        return self.FoundCycle == 0

    def DFS(self, start):
        if self.FoundCycle == 1:   return     # early stop if the loop is found    
        if self.Visited[start] == 1:
            self.FoundCycle = 1               # loop is found
        if self.Visited[start] == 0:           # node is not visited yet, visit it
            self.Visited[start] = 1             # color current node as gray
            for neib in self.adj_dict[start]:   # visit all its neibours
                self.DFS(neib)
            self.Visited[start] = 2             # color current node as black
"""
