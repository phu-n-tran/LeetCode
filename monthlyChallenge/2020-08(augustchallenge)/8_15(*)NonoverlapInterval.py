# --------------------------------------------------------------------------
# Name:        Non-overlapping Intervals
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a collection of intervals, find the minimum number of intervals 
    you need to remove to make the rest of the intervals non-overlapping.

    Example 1:
      Input: [[1,2],[2,3],[3,4],[1,3]]
      Output: 1
      Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
    
    Example 2:
      Input: [[1,2],[1,2],[1,2]]
      Output: 2
      Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

    Example 3:
      Input: [[1,2],[2,3]]
      Output: 0
      Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


    Note:
      1. You may assume the interval's end point is always bigger than its start point.
      2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]
        
        for i in range(n):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]
                
        return n - count  
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        def lis(intervals):
            n = len(intervals)
            if n <= 1:
                return 0
            
            seq = [1] * n
            # Time: O(nlogn)
            intervals.sort()
             
            max_len = 1
            for i in range(n):
                for j in range(i):
                    if not (intervals[j][0] < intervals[i][1] and intervals[j][1] > intervals[i][0]):
                        seq[i] = max(seq[i], seq[j] + 1)
                        max_len = max(max_len, seq[i])
##################################################
def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        min_heap = [intervals[0]]
        iter_intervals = iter(intervals)
        next(iter_intervals)
        ans = 0
        for interval in iter_intervals:
            if interval[0] < min_heap[0][1]:
                ans += 1
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval)
        return ans
##################################################
def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n == 0:
            return 0
        intervals = sorted(intervals)
        prev = intervals[0]
        result = 0
        for i in range(1, n):
            if prev[1] > intervals[i][0]:
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
                result += 1
            else:
                prev = intervals[i]
        return result
'''
