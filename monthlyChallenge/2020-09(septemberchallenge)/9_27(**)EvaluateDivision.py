# --------------------------------------------------------------------------
# Name:        Evaluate Division
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given an array of variable pairs equations and an array of real
    numbers values, where equations[i] = [Ai, Bi] and values[i] represent 
    the equation Ai / Bi = values[i]. Each Ai or Bi is a string that 
    represents a single variable.

    You are also given some queries, where queries[j] = [Cj, Dj] represents
    the jth query where you must find the answer for Cj / Dj = ?.

    Return the answers to all queries. If a single answer cannot be 
    determined, return -1.0.

    Note: The input is always valid. You may assume that evaluating the 
    queries will not result in division by zero and that there is no contradiction.


    Example 1:
      Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
      Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
      Explanation: 
        Given: a / b = 2.0, b / c = 3.0
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
    
    Example 2:
      Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
      Output: [3.75000,0.40000,5.00000,0.20000]
    
    Example 3:
      Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
      Output: [0.50000,2.00000,-1.00000,-1.00000]


    Constraints:
      1. 1 <= equations.length <= 20
      2. equations[i].length == 2
      3. 1 <= Ai.length, Bi.length <= 5
      4. values.length == equations.length
      5. 0.0 < values[i] <= 20.0
      6. 1 <= queries.length <= 20
      7. queries[i].length == 2
      8. 1 <= Cj.length, Dj.length <= 5
      9. Ai, Bi, Cj, Dj consist of lower case English letters and digits.
      
    Hint: Do you recognize this as a graph problem?
"""


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #1. Make Graph
        graph = {}
        for i, (num, den) in enumerate(equations):
            if num not in graph:
                graph[num] = {}
            graph[num][den] = values[i]
            
            if den not in graph:
                graph[den] = {}
            graph[den][num] = 1 / values[i]
        
        #2. Do Calculations
        result = []
        for num, den in queries:
            if num not in graph or den not in graph:
                result.append(float(-1))
            elif num == den:
                result.append(float(1))
            else:
                result.append(self.dfs(graph, num, den, 1, set()))
        
        return result
        
        
    def dfs(self, graph, start, end, prod, visited):
        visited.add(start)
        neighbors = graph[start]
        answer = float(-1)
        
        if end in neighbors:
            answer = prod * neighbors[end]
        else:
            for neighbor, value in neighbors.items():
                if neighbor not in visited:
                    answer = self.dfs(graph, neighbor, end, prod * value, visited)
                if answer != float(-1):
                    break

        return answer
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = self.build_graph(equations, values)
        output = []
        for dividend, divisor in queries:
            if dividend not in G or divisor not in G:
                res = float(-1)
            elif dividend == divisor:
                res = float(1)
            else:
                visited = set()
                res = self.backtracking(dividend, divisor, G, 1, visited)
            output.append(res)
        return output
        
    
    def build_graph(self, equations, values):
        G = defaultdict(dict)
        for i in range(len(values)):
            dividend, divisor = equations[i]
            value = values[i]
            G[dividend][divisor] = value
            G[divisor][dividend] = 1 / value
        return G
    
    def backtracking(self, cur, target, G, cur_res, visited):
        visited.add(cur)
        res = float(-1)
        neighbors = G[cur]
        if target in neighbors:
            res = cur_res * neighbors[target]
        else:
            for neighbor, val in neighbors.items():
                if neighbor in visited:
                    continue
                res = self.backtracking(neighbor, target, G, cur_res*val, visited)
                
                if res != float(-1):
                    break
        visited.remove(cur)
        return res
##################################################
def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dp  = collections.defaultdict(dict)
        for (s, t), v in zip(equations, values):
            dp[s][s] = dp[t][t] = 1.0
            dp[s][t] = v
            dp[t][s] = 1 / v
        for k in dp:
            for i in dp[k]:
                for j in dp[k]:
                    dp[i][j] = dp[i][k] * dp[k][j]
        res = []
        for s, t in queries:
            if t not in dp[s]:
                res.append(-1.0)            
            else:
                res.append(dp[s][t])        
        return res  
##################################################
def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parents = {}
        ranks = {}
        coefficients = {}

        def union(a, b, c):
            ra, ca = findroot(a)
            rb, cb = findroot(b)
            ra_to_rb = c * cb / ca
            if ra == rb: return
            rbig, rsmall, coef = (ra, rb, 1/ra_to_rb) if ranks[ra] >= ranks[rb] else (rb, ra, ra_to_rb)
            parents[rsmall] = rbig
            ranks[rbig] += ranks[rbig] == ranks[rsmall]
            coefficients[rsmall] = coef

        def findroot(a):
            if parents[a] != a:
                par, coef = findroot(parents[a])
                parents[a] = par 
                coefficients[a] *= coef
            return parents[a], coefficients[a]

        for (a, b), v in zip(equations, values):
            for el in [a, b]:
                if el not in parents:
                    parents[el] = el
                    ranks[el] = 0
                    coefficients[el] = 1
            union(a, b, v)

        res = []
        for a, b in queries:
            if a not in parents or b not in parents:
                res.append(-1)
                continue
            ra, ca = findroot(a)
            rb, cb = findroot(b)
            res.append(-1 if ra != rb else ca / cb)

        return res
##################################################
'''
