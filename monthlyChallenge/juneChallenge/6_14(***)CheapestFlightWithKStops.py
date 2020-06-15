# --------------------------------------------------------------------------
# Name:        Cheapest Flights Within K Stops
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    There are n cities connected by m flights. Each flight starts from 
    city u and arrives at v with a price w.

    Now given all the cities and flights, together with starting city src 
    and the destination dst, your task is to find the cheapest price from 
    src to dst with up to k stops. If there is no such route, output -1.

    Example 1:
        Input: 
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 1
        
        Output: 200
        Explanation: 
        The graph looks like this: (see 6_14_samples.PNG)

        The cheapest price from city 0 to city 2 with at most 1 stop
        costs 200, as marked red in the picture.

    Example 2:
        Input: 
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 0
        
        Output: 500
        Explanation: 
        The graph looks like this: (see 6_14_samples.PNG)

        The cheapest price from city 0 to city 2 with at most 0 stop costs
        500, as marked blue in the picture.


    Constraints:
        1. The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
        2. The size of flights will be in range [0, n * (n - 1) / 2].
        3. The format of each flight will be (src, dst, price).
        4. The price of each flight will be in the range [1, 10000].
        5. k is in the range of [0, n - 1].
        6. There will not be any duplicated flights or self cycles.
"""

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dist = [float("inf")]*n
        dist[src] = 0
        for _ in range(K+1):
            olddist = dist[:]
            for f in flights:
                dist[f[1]] = min(dist[f[1]], olddist[f[0]] + f[2])
        return dist[dst] if dist[dst] < float("inf") else -1
        
        
        
            
         
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        pq = []
        new_flights = dict()
             
        for u, v, w in flights:
            new_flights[u] = new_flights.get(u,[]) + [(v, w)]
            
        visited = set([])
        res = 0
        heapq.heappush(pq, (0,src,K))
        
        while pq:
            dist, node, k = heapq.heappop(pq)
            if node == dst: return dist
            visited.add(node)
            if k>=0:
                for v, w in new_flights.get(node,[]):
                    if v not in visited:
                        heapq.heappush(pq, (dist+w, v, k-1))
        return -1
##########################################################
import heapq
from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        Time: O((V + E) * log V)
        Space: O(V^2)
        """
        graph = defaultdict(dict)
        visited = {}
        for source, destination, weight in flights:
            graph[source][destination] = weight
        heap = [(0, src, 0)]
        while heap:
            price, source, nth_move = heapq.heappop(heap)
            if source == dst and K >= nth_move - 1:
                return price
            if source not in visited or visited[source] > nth_move:
                visited[source] = nth_move
                for neighbor in graph[source]:
                    heapq.heappush(heap, (graph[source][neighbor] + price, neighbor, nth_move + 1))
        return -1
'''
