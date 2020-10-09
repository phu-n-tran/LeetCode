
# --------------------------------------------------------------------------
# Name:        Remove Covered Intervals
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a list of intervals, remove all intervals that are covered by another interval in the list.

    Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

    After doing so, return the number of remaining intervals.


    Example 1:
      Input: intervals = [[1,4],[3,6],[2,8]]
      Output: 2
      Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
    
    Example 2:
      Input: intervals = [[1,4],[2,3]]
      Output: 1
    
    Example 3:
      Input: intervals = [[0,10],[5,12]]
      Output: 2
    
    Example 4:
      Input: intervals = [[3,10],[4,10],[5,11]]
      Output: 2
    
    Example 5:
      Input: intervals = [[1,2],[1,4],[3,4]]
      Output: 1

    Constraints:
      1. 1 <= intervals.length <= 1000
      2. intervals[i].length == 2
      3. 0 <= intervals[i][0] < intervals[i][1] <= 10^5
      4. All the intervals are unique.
    
    Hints:
      1. How to check if an interval is covered by another?
      2. Compare each interval to all others and check if it is covered by any interval.
"""


class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sortList = sorted(intervals, key=lambda x: (x[0], -x[1]))
        popList = []
        
        current = 0
        while current < len(sortList):
            low, high = sortList[current]
            for i in range(current+1, len(sortList)):
                if low <= sortList[i][0] and high >= sortList[i][1]:
                    popList.append(i)
            for i in sorted(popList, reverse=True):
                # print(current, i, len(sortList))
                sortList.pop(i)
            popList = []
            current += 1
            # print(sortList)
        return len(sortList)
            
            
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        left, right = -1, -1
        ans = 0
        for v in intervals:
            if v[0] > left and v[1] > right:
                left = v[0]
                ans += 1
            right = max(right, v[1])
        return ans
##################################################
def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals,key=lambda x: (x[0],-x[1]))
        count=0
        #print(intervals)
        index = 0   
        while index<len(intervals):
            low,high = intervals[index][0],intervals[index][1]
            count+=1
            index2=index+1
            while index2<len(intervals) and low<=intervals[index2][0] and high>=intervals[index2][1]:
                index2+=1
            index= index2
        return count
##################################################
def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals,key=lambda x: (x[0],-x[1]))
        count=0
        #print(intervals)
        index = 0   
        while index<len(intervals):
            low,high = intervals[index][0],intervals[index][1]
            count+=1
            index2=index+1
            while index2<len(intervals) and low<=intervals[index2][0] and high>=intervals[index2][1]:
                index2+=1
            index= index2
        return count
##################################################
'''
