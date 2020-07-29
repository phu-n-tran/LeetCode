# --------------------------------------------------------------------------
# Name:        Task Scheduler
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given a char array representing tasks CPU need to do. It contains
    capital letters A to Z where each letter represents a different task. 
    Tasks could be done without the original order of the array. Each task 
    is done in one unit of time. For each unit of time, the CPU could complete
    either one task or just be idle.

    However, there is a non-negative integer n that represents the cooldown
    period between two same tasks (the same letter in the array), that is 
    that there must be at least n units of time between any two same tasks.

    You need to return the least number of units of times that the CPU will 
    take to finish all the given tasks.

    Example 1:
      Input: tasks = ["A","A","A","B","B","B"], n = 2
      Output: 8
      Explanation: 
        A -> B -> idle -> A -> B -> idle -> A -> B
        There is at least 2 units of time between any two same tasks.
    
    Example 2:
      Input: tasks = ["A","A","A","B","B","B"], n = 0
      Output: 6
      Explanation: On this case any permutation of size 6 would work since n = 0.
        ["A","A","A","B","B","B"]
        ["A","B","A","B","A","B"]
        ["B","B","B","A","A","A"]
        ...
        And so on.
    
    Example 3:
      Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
      Output: 16
      Explanation: 
        One possible solution is
        A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

    Constraints:
      1. The number of tasks is in the range [1, 10000].
      2. The integer n is in the range [0, 100].
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)
        Most_freq = freq.most_common()[0][1]
        Found_most = sum([freq[key] == Most_freq for key in freq])
        return max(len(tasks), (Most_freq - 1) * (n + 1) + Found_most)
        
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def leastInterval(self, tasks, n):
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
##################################################
def leastInterval(self, tasks, n):
        frequencies=[0]*26
        for t in tasks:
            frequencies[ord(t)-ord('A')]+=1
        frequencies.sort()
        f_max=frequencies.pop() 
        idle_time=(f_max-1)*n
        while frequencies and idle_time>0:
            idle_time-=min(f_max-1,frequencies.pop())
        idle_time=max(0,idle_time)
        return idle_time+len(tasks)
##################################################
def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        arr = []
        counts = [0 for i in range(26)]
        
        for t in tasks:
            counts[ord(t)-ord('A')] += 1
            
        maxcount = max(counts)
        maxnum = 0
        for c in counts:
            if c == maxcount:
                maxnum += 1
        
        empty = (n-maxnum+1)*(maxcount-1)
        
        if empty < 0:
            return len(tasks)
        
        for c in counts:
            if c != maxcount:
                empty -= min(maxcount-1, c)
        if empty < 0:
            return len(tasks)
        return len(tasks) + empty
'''
