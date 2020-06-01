# --------------------------------------------------------------------------
# Name:        First Unique Character in String
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a set of N people (numbered 1, 2, ..., N), we would like to split
    everyone into two groups of any size.

    Each person may dislike some other people, and they should not go into 
    the same group. 

    Formally, if dislikes[i] = [a, b], it means it is not allowed to put 
    the people numbered a and b into the same group.

    Return true if and only if it is possible to split everyone into two
    groups in this way.

    Example 1:
        Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
        Output: true
        Explanation: group1 [1,4], group2 [2,3]
        
    Example 2:
        Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
        Output: false
   
    Example 3:
        Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
        Output: false


    Constraints:
        1. 1 <= N <= 2000
        2. 0 <= dislikes.length <= 10000
        3. dislikes[i].length == 2
        4. 1 <= dislikes[i][j] <= N
        5. dislikes[i][0] < dislikes[i][1]
        6. There does not exist i != j for which dislikes[i] == dislikes[j].
"""

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        def visited(graph, vertex, color, visit):
            visit[vertex] = color
            
            for adj_v in graph.get(vertex, []):
                if visit[adj_v] == color:
                    return False
                
                if visit[adj_v] == 0 and not visited(graph, adj_v, -color, visit):
                    return False
            return True
        
            
        if N < 3 or len(dislikes) < 2:
            return True
        
        graph = {}
        for p1, p2 in dislikes:
            graph[p1] = graph.get(p1, []) + [p2]
            graph[p2] = graph.get(p2, []) + [p1]

        visit = [0 for _ in range(N+1)]
        
        for i in range(1, N+1):
            if visit[i] == 0 and not visited(graph, i, 1, visit):
                return False
        return True
    
            
        
        
        
        
        
        
        
"""other faster methods (from other submissions)
##################################################
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        groups = [0] * (N+1)
        graph = collections.defaultdict(list)
        for dis in dislikes:
            a, b = dis
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i):
            for nei in graph[i]:
                if not groups[nei]:
                    groups[nei] = -groups[i]
                    if not dfs(nei):
                        return False
                else:
                    if groups[nei] == groups[i]:
                        return False
                    
            return True
        
        for i in range(1, N+1):
            if groups[i] == 0:
                groups[i] = 1
                if not dfs(i):
                    return False
        return True
"""
