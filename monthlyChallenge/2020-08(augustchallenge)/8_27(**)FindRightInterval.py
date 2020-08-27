# --------------------------------------------------------------------------
# Name:        Find Right Interval
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a set of intervals, for each of the interval i, check if there 
    exists an interval j whose start point is bigger than or equal to the
    end point of the interval i, which can be called that j is on the "right" of i.

    For any interval i, you need to store the minimum interval j's index, 
    which means that the interval j has the minimum start point to build 
    the "right" relationship for interval i. If the interval j doesn't exist,
    store -1 for the interval i. Finally, you need output the stored value of
    each interval as an array.

    Note:
      1. You may assume the interval's end point is always bigger than its start point.
      2. You may assume none of these intervals have the same start point.

    Example 1:
      Input: [ [1,2] ]
      Output: [-1]
      Explanation: There is only one interval in the collection, so it outputs -1.

    Example 2:
      Input: [ [3,4], [2,3], [1,2] ]
      Output: [-1, 0, 1]
      Explanation: There is no satisfied "right" interval for [3,4].
        For [2,3], the interval [3,4] has minimum-"right" start point;
        For [1,2], the interval [2,3] has minimum-"right" start point.

    Example 3:
      Input: [ [1,4], [2,3], [3,4] ]
      Output: [-1, 2, -1]
      Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
        For [2,3], the interval [3,4] has minimum-"right" start point.
        NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        start_q = []
        end_q = []
        res = [-1] * len(intervals)
        for i, interval in enumerate(intervals):
            heapq.heappush(start_q, (interval[0], i))
            heapq.heappush(end_q, (interval[1], i))
        
        while end_q and start_q:
            end, end_index = heapq.heappop(end_q)
            while start_q:
                start, start_index = start_q[0][0], start_q[0][1]
                if start < end:
                    heapq.heappop(start_q)
                    continue
                res[end_index] = start_index
                break
            
        return res
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        first=[]
        inmap={}
        for i,p in enumerate(intervals):
            first.append(p[0])
            inmap[p[0]]=i
        first.sort()
        res=[]
        for p in intervals:
            pos=bisect_left(first,p[1])
            if pos>=len(first):
                res.append(-1)
            else:
                res.append(inmap[first[pos]])
        return res
##################################################
def findRightInterval(self, intervals): # nlogn+nlogn       
        interval_dict = {} # start, index of interval
        for i, (start, _) in enumerate(intervals):
            interval_dict[start] = i
            
        sorted_start_list = sorted([interval[0] for interval in intervals]) # sorted list of strt point         
        res = []        
        for start, end in intervals:
            if end in interval_dict: #if any interval start is same as curr_end, then strt interval indx is right interval for cur interval
                res.append(interval_dict[end])
                continue # we got the right interval so skip
            idx = bisect.bisect_left(sorted_start_list, end) # else, find curr end position in sorted strt list
            #print(idx,end,sorted_start_list)
            if idx == len(intervals):# if curr end position is at last in sorted strt then no right interval
                res.append(-1)
            else:
                res.append(interval_dict[sorted_start_list[idx]]) # else get the index of start point where positioning the cur end strt list remains sorted, add tht strt index into result
        return res
##################################################

'''
