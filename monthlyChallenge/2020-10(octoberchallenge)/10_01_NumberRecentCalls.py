
# --------------------------------------------------------------------------
# Name:        Number of Recent Calls (Iteration over Sliding Window)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You have a RecentCounter class which counts the number of recent requests
    within a certain time frame.

    Implement the RecentCounter class:
      - RecentCounter() Initializes the counter with zero recent requests.
      - int ping(int t) Adds a new request at time t, where t represents some
        time in milliseconds, and returns the number of requests that has 
        happened in the past 3000 milliseconds (including the new request). 
        Specifically, return the number of requests that have happened in the 
        inclusive range [t - 3000, t]. It is guaranteed that every call to 
        ping uses a strictly larger value of t than the previous call.

    Example 1:
      Input
        ["RecentCounter", "ping", "ping", "ping", "ping"]
        [[], [1], [100], [3001], [3002]]
      Output
        [null, 1, 2, 3, 3]
      Explanation
        RecentCounter recentCounter = new RecentCounter();
        recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
        recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
        recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
        recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

    Constraints:
      1. 1 <= t <= 109
      2. Each test case will call ping with strictly increasing values of t.
      3. At most 104 calls will be made to ping.
"""


class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # hint: the lower bound will always keep increasing.
        # As for the upper bound it always include the newest t. 
        # So only need to check and remove the lower bound by using deque
        lower = t - 3000
        self.queue.append(t)

        while len(self.queue) > 0 and self.queue[0] < lower:
            self.queue.pop(0) # dequeue
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
class RecentCounter(object):

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # step 1). append the current call
        self.slide_window.append(t)

        # step 2). invalidate the outdated pings
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()

        return len(self.slide_window)
##################################################

##################################################

##################################################
'''
