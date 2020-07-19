
# --------------------------------------------------------------------------
# Name:        Course Schedule II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take course 0 you
    have to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, 
    return the ordering of courses you should take to finish all courses.

    There may be multiple correct orders, you just need to return one of 
    them. If it is impossible to finish all courses, return an empty array.

    Example 1:
      Input: 2, [[1,0]] 
      Output: [0,1]
      Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
                   course 0. So the correct course order is [0,1] .
  
    Example 2:
      Input: 4, [[1,0],[2,0],[3,1],[3,2]]
      Output: [0,1,2,3] or [0,2,1,3]
      Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
                   courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
                   So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

    Note:
      1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
      2. You may assume that there are no duplicate edges in the input prerequisites.
      
    Hints:
      1. This problem is equivalent to finding the topological order in a directed graph.
         If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
      2. Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
      3. Topological sort could also be done via BFS.
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.adj_dict = defaultdict(set)
        for i, j in prerequisites:
            self.adj_dict[i].add(j)

        self.Visited = [0] * numCourses
        self.Ans, self.FoundCycle = [], 0
        
        for i in range(numCourses):
            if self.FoundCycle == 1: break      # early stop if the loop is found
            if self.Visited[i] == 0:
                self.dfs(i)
     
        return [] if self.FoundCycle == 1 else self.Ans

    def dfs(self, start):
        if self.FoundCycle == 1:   return     # early stop if the loop is found    
        if self.Visited[start] == 1:
            self.FoundCycle = 1               # loop is found
        if self.Visited[start] == 0:           # node is not visited yet, visit it
            self.Visited[start] = 1             # color current node as gray
            for neib in self.adj_dict[start]:   # visit all its neibours
                self.dfs(neib)
            self.Visited[start] = 2             # color current node as black
            self.Ans.append(start)              # add node to answer
        
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other  methods (from other submissions)
##################################################
def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inDegree = [0]*numCourses
        graph = [set() for _ in range(numCourses)]
        for course,preReq in prerequisites:
            graph[preReq].add(course)
            inDegree[course] += 1
            
        roots = [v for v in range(numCourses) if inDegree[v] == 0]
        courseOrder = []

        while(roots):
            root = roots.pop(0)
            courseOrder.append(root)
            for course in graph[root]:
                inDegree[course] -= 1
                if(inDegree[course] == 0):
                    roots.append(course)
        if(len(courseOrder) != numCourses):
            return []
        else:
            return courseOrder
##################################################
def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        queue = collections.deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            course = queue.popleft()
            ans.append(course)
            for i in graph[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
                    
        if len(ans) == numCourses:
            return ans
        
        return []
##################################################

'''
