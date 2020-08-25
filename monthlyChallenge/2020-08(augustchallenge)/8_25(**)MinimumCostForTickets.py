# --------------------------------------------------------------------------
# Name:        Minimum Cost For Tickets
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    In a country popular for train travel, you have planned some train 
    travelling one year in advance.  The days of the year that you will 
    travel is given as an array days.  Each day is an integer from 1 to 365.

    Train tickets are sold in 3 different ways:

    a 1-day pass is sold for costs[0] dollars;
    a 7-day pass is sold for costs[1] dollars;
    a 30-day pass is sold for costs[2] dollars.
    The passes allow that many days of consecutive travel.  
      For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the given list of days.

 
    Example 1:
      Input: days = [1,4,6,7,8,20], costs = [2,7,15]
      Output: 11
      Explanation: 
        For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
        On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
        On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
        In total you spent $11 and covered all the days of your travel.
    
    Example 2:
      Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
      Output: 17
      Explanation: 
        For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
        On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
        In total you spent $17 and covered all the days of your travel.
        
    Note:
      1. 1 <= days.length <= 365
      2. 1 <= days[i] <= 365
      3. days is in strictly increasing order.
      4. costs.length == 3
      5. 1 <= costs[i] <= 1000
"""


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        in_days = {d: True for d in days} #(1)
        max_day = max(days)
        dp = [0 for i in range(max_day + 1)] #(2)
        dp[0] = 0 #(3)
        
        for i in range(len(dp)):
            if in_days.get(i):
                pass1 = dp[i - 1] if i - 1 > 0 else 0 #(3)
                pass7 = dp[i - 7] if i - 7 > 0 else 0
                pass30 = dp[i - 30] if i - 30 > 0 else 0
                
                dp[i] = min(pass1 + costs[0],
                           pass7 + costs[1],
                           pass30 + costs[2]) #(4)
            else:
                dp[i] = dp[i - 1] #(5)
        
        return dp[max_day]
    
    #(1) Now we can check if a day is in days in constant time.
    #(2) dp[i] = minimum cost to travel up until days[i]
    #(3) A negative day is the equivalent to starting at day 0.
    #(4) The cost to travel to day i using a 1-day pass is the minimum cost to travel
    #    until day i - 1 plus the cost for a 1-day pass. Apply this logic to the other passes. 
    #    Because we want to know the minimum cost to travel up until day i, we must take the minimum of the 3 possible ways.
    #(5) If day i isn't a day we need to travel on, then we shouldn't travel. 
    #    But we can't just set dp[i] = 0. That would be saying we spent $0 to travel
    #    up until day i when we may have actually spent more than $0. Instead, we should 
    #    set dp[i] = dp[i - 1]. Try to reason through this using common sense: if you spent $15
    #    yesterday and $0 today, how much money did you spend up until today?
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        max_day = days[-1]+1
        dp = [0]*(max_day)
        set_days = set(days)
        cost = costs[0]
        for i in xrange(1,max_day):
            if i not in set_days:
                dp[i] = dp[i-1]
                continue
            one = dp[i-1]+costs[0]
            seven = dp[max(i-7,0)]+costs[1]
            thirty = dp[max(i-30,0)]+costs[2]
            dp[i] = min(one, seven, thirty)
        return dp[-1]
##################################################
def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        length = days[-1]
        dp = [0] * (length + 1)
        
        for i in range(1, length + 1):
            if i not in days:
                dp[i] = dp[i-1]
            
            else:
                dp[i] = min(
                    dp[i-1] + costs[0], 
                    dp[max(0, i-7)] + costs[1], 
                    dp[max(0, i-30)] + costs[2]
                )
        
        return dp[length]
##################################################
def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        last_day = days[-1]
        dp = [0] * (last_day + 1) 
        days = set(days) # convert day to set for fast look up later
        for d in range(1, last_day + 1):
            # to make sure we have pass, we either buy a 1-d pass today, a 7-d pass 6 days ago, or a 30-d pass 29 days ago
            if d in days:
                dp[d] = min(costs[2] + dp[max(d - 30, 0)], costs[1] + dp[max(d - 7, 0)], costs[0] + dp[d - 1])
            else: # we don't buy pass on day not in days
                dp[d] = dp[d - 1]
        return dp[-1]
'''
