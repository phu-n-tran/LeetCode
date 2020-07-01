# --------------------------------------------------------------------------
# Name:        Reconstruct Itinerary
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a list of airline tickets represented by pairs of departure and 
    arrival airports [from, to], reconstruct the itinerary in order. All of
    the tickets belong to a man who departs from JFK. Thus, the itinerary 
    must begin with JFK.

    Note:
      1. If there are multiple valid itineraries, you should return the 
         itinerary that has the smallest lexical order when read as a single 
         string. For example, the itinerary ["JFK", "LGA"] has a smaller 
         lexical order than ["JFK", "LGB"].
      2. All airports are represented by three capital letters (IATA code).
      3. You may assume all tickets form at least one valid itinerary.
      4. One must use all the tickets once and only once.
   
    Example 1:
      Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
      Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
    
    Example 2:
      Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
      Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
      Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                   But it is larger in lexical order.
"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(cur_airport, adjList, path):
            
            while adjList.get(cur_airport, []):
                # remove the last element since it is sort in descending and it is to ensure the result contains the smallest lexical order
                next_des = adjList[cur_airport].pop()
                dfs(next_des, adjList, path)
            path.append(cur_airport)
            
        
        adjList = dict()
        path = []
        
        for src, des in tickets:
            adjList[src] = adjList.get(src, []) + [des]
        # sort by descending order, since the last des is recorded first
        for key in adjList:
            adjList[key].sort(reverse=True)

        dfs("JFK", adjList, path)
        # reverse the list
        return path[::-1]
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        from collections import defaultdict
        d = defaultdict(list)
        for i in sorted(tickets):
            d[i[0]].append(i[1])
        res = []
        
        def dfs(airport):
            
            while(d[airport]):
                v = d[airport].pop(0)
                dfs(v)
                res.append(v)
        

        dfs('JFK')
        res.append('JFK')
        print(res)
        return res[::-1]
##################################################
def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        airports={}
        for dep,arr in tickets:
            if dep not in airports:
                airports[dep]=[arr]
            else:
                heappush(airports[dep],arr)
            if arr not in airports:
                airports[arr]=[]
        
        return self.dfs(airports,"JFK",[])[::-1]
    
    def dfs(self,airports,departure,res):
        while airports[departure]:
            self.dfs(airports,heappop(airports[departure]),res)
        res.append(departure)
        return res
'''
