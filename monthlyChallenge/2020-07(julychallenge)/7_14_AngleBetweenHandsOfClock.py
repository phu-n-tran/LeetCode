# --------------------------------------------------------------------------
# Name:        Angle Between Hands of a Clock
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two numbers, hour and minutes. Return the smaller angle (in degrees) 
    formed between the hour and the minute hand.

    Example 1:
      Input: hour = 12, minutes = 30
      Output: 165

    Example 2:
      Input: hour = 3, minutes = 30
      Output: 75

    Example 3:
      Input: hour = 3, minutes = 15
      Output: 7.5

    Example 4:
      Input: hour = 4, minutes = 50
      Output: 155

    Example 5:
      Input: hour = 12, minutes = 0
      Output: 0

    Constraints:
      1. 1 <= hour <= 12
      2. 0 <= minutes <= 59
      3. Answers within 10^-5 of the actual value will be accepted as correct.
      
    Hints:
      1. The tricky part is determining how the minute hand affects the position of the hour hand.
      2. Calculate the angles separately then find the difference.
"""


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # small increment is 6 degree, from 1 to 2 is 30 degree
        shiftOfHour = (minutes / 60.0) * 5
        
        if hour == 12:
            hour = 0
        
        # convert hour to minutes
        hour *= 5
        hour += shiftOfHour
        print(hour, minutes)
        print(abs(hour-minutes), 60-abs(hour-minutes))
        
        # choose the smaller angle and convert it from minutes to degree
        # inside min() use 60 beacause everything is in minutes and there are 60 minutes marks showing on the clock
        return min(abs(hour-minutes), 60-abs(hour-minutes)) * 6
    
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle_hour = float(hour) * 360. / 12.
        angle_hour += float(minutes) / 60. * 360. / 12.
        angle_minutes = float(minutes) / 60. * 360.
        ans = abs(angle_hour - angle_minutes)
        if ans > 180:
            ans = 360 - ans
            
        return ans
##################################################
def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minutes_degree = 360 * float(minutes) / 60
        hour_degree = 30 * (hour % 12) + minutes_degree / 12
        abs_diff = abs(hour_degree - minutes_degree)
        return min(abs_diff, 360 - abs_diff)
##################################################
def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minute_angle = minutes / 60.0 * 360
        modified_hour_angle = hour/12.0 * 360 + ((minutes / 60.0) * 360.0 / 12.0)
        abs_diff = abs(minute_angle - modified_hour_angle)
        if abs_diff > 180:
            return 360 - abs_diff
        else:
            return abs_diff
'''
