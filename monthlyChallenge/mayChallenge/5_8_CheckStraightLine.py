# --------------------------------------------------------------------------
# Name:        Check if all points are in a straight line
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
    represents the coordinate of a point. Check if these points make a 
    straight line in the XY plane.
    
    Example 1:
        Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
        Output: true
    
    Example 2:
        Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        Output: false
    
    Constraints:
        1) 2 <= coordinates.length <= 1000
        2) coordinates[i].length == 2
        3) -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
        4) coordinates contains no duplicate point.
"""
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True
        
        delta_x = coordinates[0][0] - coordinates[1][0]
        delta_y = coordinates[0][1] - coordinates[1][1]
        
        # if dx == 0, mean that the straight line is vertical
        if delta_x == 0:
            return len({point[0] for point in coordinates}) == 1
        # if dy == 0, mean that the straight line is horizontal
        elif delta_y == 0:
            return len({point[1] for point in coordinates}) == 1
        else:
            slope = delta_y/delta_x

            for i in range(2, len(coordinates)):
                x = coordinates[i-1][0] - coordinates[i][0]
                y = coordinates[i-1][1] - coordinates[i][1]
                if x == 0 or y == 0:
                    return False
                new_slope = y / x
                if slope != new_slope:
                    return False

        return True
        
"""My other slower solution
def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True
        
        delta_x = coordinates[0][0] - coordinates[1][0]
        delta_y = coordinates[0][1] - coordinates[1][1]
        
        # if dx == 0, mean that the straight line is vertical
        if delta_x == 0:
            return len({point[0] for point in coordinates}) == 1
        # if dy == 0, mean that the straight line is horizontal
        elif delta_y == 0:
            return len({point[1] for point in coordinates}) == 1
        else:
            try:
                slope = delta_y/delta_x
            
                for i in range(2, len(coordinates)):
                    x = coordinates[i-1][0] - coordinates[i][0]
                    y = coordinates[i-1][1] - coordinates[i][1]

                    new_slope = y / x
                    if slope != new_slope:
                        return False
            except ZeroDivisionError:
                return False

        return True


other faster methods (from other submissions)
##################################################
def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        p1=coordinates[0]
        p2=coordinates[1]
        if p1[0]-p2[0] == 0: slope = sys.maxint
        else: slope=float((p1[1]-p2[1]))/float((p1[0]-p2[0]))
        for p2 in coordinates[2:]:
            if p1[0]-p2[0] == 0: slope = sys.maxint
            else: s=float((p1[1]-p2[1]))/float((p1[0]-p2[0]))
            if s!=slope: return False
        return True
 ###################################################
     def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        if coordinates[1][0] == coordinates[0][0]:
            #All points must be on a vertical line
            return len(set([p[0] for p in coordinates])) == 1
        
        
        m = float(coordinates[1][1] - coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        b = coordinates[1][1] - m*coordinates[1][0]
        
        for i in range(2, len(coordinates)):
            if abs(coordinates[i][1] - m*coordinates[i][0] - b) != 0:
                return False
            
        return True
"""

