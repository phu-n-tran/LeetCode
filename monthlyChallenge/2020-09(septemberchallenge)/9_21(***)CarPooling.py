# --------------------------------------------------------------------------
# Name:        Car Pooling
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are driving a vehicle that has capacity empty seats initially 
    available for passengers.  The vehicle only drives east 
    (ie. it cannot turn around and drive west.)

    Given a list of trips, trip[i] = [num_passengers, start_location, 
    end_location] contains information about the i-th trip: the number
    of passengers that must be picked up, and the locations to pick them
    up and drop them off.  The locations are given as the number of
    kilometers due east from your vehicle's initial location.

    Return true if and only if it is possible to pick up and drop off all 
    passengers for all the given trips. 


    Example 1:
      Input: trips = [[2,1,5],[3,3,7]], capacity = 4
      Output: false
    
    Example 2:
      Input: trips = [[2,1,5],[3,3,7]], capacity = 5
      Output: true
    
    Example 3:
      Input: trips = [[2,1,5],[3,5,7]], capacity = 3
      Output: true

    Example 4:
      Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
      Output: true

    Constraints:
      1. trips.length <= 1000
      2. trips[i].length == 3
      3. 1 <= trips[i][0] <= 100
      4. 0 <= trips[i][1] < trips[i][2] <= 1000
      5. 1 <= capacity <= 100000
     
    Hint:
      1. Sort the pickup and dropoff events by location, then process them in order.
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        final_max = float('-inf')
        for seats, start_time, end_time in trips:
            final_max = max(final_max, end_time)
        seat_arr = [0] * (final_max + 1)
        for seats, start_time, end_time in trips:
            cur_time = start_time
            while cur_time < end_time:
                seat_arr[cur_time] += seats
                cur_time += 1
        return all([seats <= capacity for seats in seat_arr])
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        times = [0]*1001
        
        for trip in trips:
            times[trip[1]] += trip[0]
            times[trip[2]] -= trip[0]
        
        curr_load = 0
        for change in times:
            curr_load += change
            if curr_load > capacity:
                return False
        
        return True
##################################################
def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        mapping = defaultdict(int)
        spots = set()
        for trip in trips:
            num = trip[0]
            start = trip[1]
            end = trip[2]

            mapping[start] += num
            mapping[end] -= num
            spots.add(start)
            spots.add(end)
        currentNum = 0
        for i in sorted(list(spots)):
            currentNum += mapping[i]
            if currentNum > capacity:
                return False
        return True 
##################################################
def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
            #print(lst)
        lst.sort()
        #print(lst)
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
##################################################
'''
