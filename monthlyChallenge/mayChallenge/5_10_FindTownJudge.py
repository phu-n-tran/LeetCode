# --------------------------------------------------------------------------
# Name:        Find the Town Judge
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    In a town, there are N people labelled from 1 to N.  There is a rumor 
    that one of these people is secretly the town judge.

    If the town judge exists, then:
        1) The town judge trusts nobody.
        2) Everybody (except for the town judge) trusts the town judge.
        3) There is exactly one person that satisfies properties 1 and 2.
    
    You are given trust, an array of pairs trust[i] = [a, b] representing
    that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the 
    town judge.  Otherwise, return -1.
    
    Example 1:
        Input: N = 2, trust = [[1,2]]
        Output: 2
    
    Example 2:
        Input: N = 3, trust = [[1,3],[2,3]]
        Output: 3
    
    Example 3:
        Input: N = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1
        
    Example 4:
        Input: N = 3, trust = [[1,2],[2,3]]
        Output: -1
        
    Example 5:
        Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        Output: 3
    
    Note: 
        1) 1 <= N <= 1000
        2) trust.length <= 10000
        3) trust[i] are all different
        4) trust[i][0] != trust[i][1]
        5) 1 <= trust[i][0], trust[i][1] <= N
"""
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) == 1:
            return trust[0][1]
        
        d = {}
        for i in trust:
            d[i[0]] = d.get(i[0], []) + [i[1]]
        
        if len(d) == N:
            return -1
        
        missing = [i for i in range(1, N+1) if i not in d]
        
        result = -1
        for i in missing:
            result = i
            for key in d:
                if i not in d[key]:
                    result = -1
                    break
        
        return result
                    
    
    










        
"""other faster methods (from other submissions)
##################################################
  def findJudge(self, N, trust):
      """
      :type N: int
      :type trust: List[List[int]]
      :rtype: int
      """
      if N == 1:
          return 1

      in_degrees = [0 for _ in range(N+1)]
      out_degrees = [0 for _ in range(N+1)]
      for a, b in trust:
          in_degrees[b] += 1
          out_degrees[a] += 1

      for i in range(1, N+1):
          if in_degrees[i] == N-1 and out_degrees[i] == 0:
              return i

      return -1
"""
