# --------------------------------------------------------------------------
# Name:        Insert Interval
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a set of non-overlapping intervals, insert a new interval into 
    the intervals (merge if necessary).

    You may assume that the intervals were initially sorted according to
    their start times.

    Example 1:
      Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
      Output: [[1,5],[6,9]]
    
    Example 2:
      Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
      Output: [[1,2],[3,10],[12,16]]
      Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    
    Example 3:
      Input: intervals = [], newInterval = [5,7]
      Output: [[5,7]]
    
    Example 4:
      Input: intervals = [[1,5]], newInterval = [2,3]
      Output: [[1,5]]
    
    Example 5:
      Input: intervals = [[1,5]], newInterval = [2,7]
      Output: [[1,7]]


    Constraints:
      1. 0 <= intervals.length <= 104
      2. intervals[i].length == 2
      3. 0 <= intervals[i][0] <= intervals[i][1] <= 105
      4. intervals is sorted by intervals[i][0] in ascending order.
      5. newInterval.length == 2
      6. 0 <= newInterval[0] <= newInterval[1] <= 105
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                res.append([x, y])
            elif newInterval[1] < x:
                i -= 1
                break
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
                
        return res + [newInterval] + intervals[i+1:]
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Input: intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]],
        # newInterval =               [4,           8]
        # Output:            [[1,2], [3,              10], [12,16]]
        # Explanation: Because the new interval[4, 8] overlaps with [3, 5], [6, 7], [8, 10].

        if len(intervals) == 0:
            return [newInterval]

        output = []
        # new interval = [L, H]
        L = newInterval[0]
        H = newInterval[1]
        # after adjustment
        L_final = 0
        H_final = 0
        # overlap condition - assume (x,y) are endpoints of current interval
        # overlap occurs if either endpoint is inside interval i.e.:
        # L < x < H or L < y < H
        overlap = False
        overlap_not_detected = True
        for interval in intervals:
            x = interval[0]
            y = interval[1]

            if not ((y < L) or (H < x)):
                # overlap case
                if overlap:
                    # if overlap already detected
                    # we know L < x
                    if (y <= H):
                        continue
                    # ending overlap
                    if H < x:
                        output.append([L_final, H_final])
                        overlap = False
                        continue
                    elif H == x:
                        H_final = y
                        output.append([L_final, H_final])
                        overlap = False
                        continue
                    elif (x < H) and (y > H):
                        H_final = y
                        output.append([L_final, H_final])
                        overlap = False
                        continue
                else:
                    if (L <= y):
                        H_final = max(y,H)
                        L_final = min(x,L)
                        overlap = True
                        overlap_not_detected = False
                        continue
            # no overlap cases
            # y < L or H < x
            if (y < L) or (H < x):
                if overlap:
                    output.append([L_final, H_final])
                    overlap = False
                output.append(interval)
                continue

        if overlap:
            output.append([L_final, H_final])

        if overlap_not_detected:
            output.append(newInterval)

        output = sorted(output, key = lambda l:l[0])
        return output
##################################################
def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        r=[]
        idx = 0
        n = len(intervals)
        while idx < n and intervals[idx][1] < newInterval[0]:
            r.append(intervals[idx])
            idx+=1
        # print("0: idx="+str(idx))
        if idx == n:
            # print("1: idx="+str(idx))
            r.append(newInterval)
            return r
        if intervals[idx][0] > newInterval[1]:
            # print("2: idx= "+str(idx)+", add "+str(newInterval)+" to "+ str(r))
            r.append(newInterval)
            r+=intervals[idx:]
            return r
        # print("3: idx="+str(idx))
        b = min(intervals[idx][0],newInterval[0])
        e = newInterval[1]
        # print("4: [b,e]=["+str(b)+","+str(e)+"]")
        while idx < n and intervals[idx][1] <= e:
            idx+=1
        # print("5: idx="+str(idx))
        if idx < n and e >= intervals[idx][0]:
            e = intervals[idx][1]
            idx+=1
        r.append([b,e])
        r+=intervals[idx:]
        return r
##################################################
def insert(self, itvs, newItv):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = [], []
        start, end = newItv[0], newItv[1]
        for i in itvs:
            if i[1] < start:
                left.append(i)
            elif i[0] > end:
                right.append(i)
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        return left + [[start, end]] + right
##################################################
def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if s > i[1]:
                left += i,
            elif e < i[0]:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s, e]] + right
'''
