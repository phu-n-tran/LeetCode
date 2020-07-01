# --------------------------------------------------------------------------
# Name:        Delete Node in a Linked List
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    There are 2N people a company is planning to interview. The cost of 
    flying the i-th person to city A is costs[i][0], and the cost of flying
    the i-th person to city B is costs[i][1].

    Return the minimum cost to fly every person to a city such that exactly
    N people arrive in each city.
    
    Example 1:
        Input: [[10,20],[30,200],[400,50],[30,20]]
        Output: 110
        Explanation: 
            The first person goes to city A for a cost of 10.
            The second person goes to city A for a cost of 30.
            The third person goes to city B for a cost of 50.
            The fourth person goes to city B for a cost of 20.

            The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half
            the people interviewing in each city.
   
    Implementation explanation:
        Input: [[10,20],[30,200],[400,50],[30,20]]
        1) if all people (2N) go to city A: 10 + 30 + 400 + 30 
        2) find difference for each element: 10, 170, -350, -10
        3) get the sum of half of the smallest elements: -350 + -10
        4) add 1) and 3) together to get the lowest cost that N people went to A city and N people went to B city
   
   Note:
      1. 1 <= costs.length <= 100
      2. It is guaranteed that costs.length is even.
      3. 1 <= costs[i][0], costs[i][1] <= 1000
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        mid = len(costs)//2
        
        # first, assume all people go to city A
        costA = sum(a for a,b in costs)
        
        # second, take the diff (b-a) for each element and then sort it in ASC 
        # -> positive means that we have to pay extra if we went to b instead of a at index i
        # -> negative means that we can save money if we went to b instead of a at index i
        BDiffA = sum(sorted(b-a for a,b in costs)[:mid])
        
        # since we need N in A and N in B, we take total cost if 2N people went to A + BDiffA
        # -> BDiffA is positive means that we need to pay extra since we need N people in A and N in B
        # -> BDiffA is negative means that we can reduce the cost if we take B instead of A
        return costA + BDiffA
        
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs) / 2
        costs = sorted(costs, key = lambda x:abs(x[0] - x[1]), reverse=True)
        aCount = 0
        bCount = 0
        ans = 0
        for c in costs:
            if c[0] < c[1]:
                if aCount < n:
                    aCount += 1
                    ans += c[0]
                else:
                    bCount += 1
                    ans += c[1]
            else:
                if bCount < n:
                    bCount += 1
                    ans += c[1]
                else:
                    aCount += 1
                    ans += c[0]
        return ans
'''
