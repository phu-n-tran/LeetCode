# --------------------------------------------------------------------------
# Name:        Robot Bounded In Circle
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    On an infinite plane, a robot initially stands at (0, 0) and faces north.
    The robot can receive one of three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degress to the right.
    The robot performs the instructions given in order, and repeats them forever.

    Return true if and only if there exists a circle in the plane such that 
    the robot never leaves the circle.

    Example 1:
      Input: "GGLLGG"
      Output: true
      Explanation: 
        The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
        When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

    Example 2:
      Input: "GG"
      Output: false
      Explanation: 
        The robot moves north indefinitely.

    Example 3:
      Input: "GL"
      Output: true
      Explanation: 
        The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

    Note:
      1. 1 <= instructions.length <= 100
      2. instructions[i] is in {'G', 'L', 'R'}
    
    Hints:
      1. Calculate the final vector of how the robot travels after executing all 
         instructions once - it consists of a change in position plus a change in direction.
      2. The robot stays in the circle iff (looking at the final vector) it changes direction
         (ie. doesn't stay pointing north), or it moves 0.
"""


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direction = (0,1)
        start = [0,0]
        
        for x in instructions:
            if x == 'G':
                start[0] += direction[0]
                start[1] += direction[1]
            elif x == 'L':
                direction = (-direction[1], direction[0])
            elif x == 'R':
                direction = (direction[1], -direction[0])
        
        return start == [0,0] or direction != (0,1)
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # 0=N, 1=E, 2=S, 3=W
        direction = 0
        spot = [0,0]
        for i in instructions:
            # spots.add(spot)
            if i == 'L':
                direction = (direction-1) %4
            if i == 'R':
                direction = (direction+1) %4
            if i == 'G':
                if direction == 0:
                    spot = [spot[0], spot[1]+1]
                if direction == 1:
                    spot = [spot[0]+1, spot[1]]
                if direction == 2:
                    spot = [spot[0], spot[1]-1]
                if direction == 3:
                    spot = [spot[0]-1, spot[1]]    
        if spot == [0,0] or direction != 0:
            return True
        return False
##################################################
def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        pos = start = (0, 0)
        vec = (0, 1)
        for i in range(len(instructions)):
            a = instructions[i]
            if a == "G":
                pos = (pos[0] + vec[0], pos[1] + vec[1])
            if a == 'L':
                if vec == (0, 1): vec = (-1, 0)
                elif vec == (-1, 0): vec = (0, -1)
                elif vec == (0, -1): vec = (1, 0)
                elif vec == (1, 0): vec = (0, 1)
            if a == 'R':
                if vec == (0, 1): vec = (1, 0)
                elif vec == (1, 0): vec = (0, -1)
                elif vec == (0, -1): vec = (-1, 0)
                elif vec == (-1, 0): vec = (0, 1)
        print(pos, vec)
        return pos == start or vec != (0, 1)
##################################################
def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        x, y = 0, 0
        curd = 0
        for i in instructions:
            if i == "G":
                x += dirs[curd][0]
                y += dirs[curd][1]
            elif i == "L":
                curd = (curd + 3) % 4
            elif i == "R":
                curd = (curd + 1) % 4
            # print curd
        return (x == 0 and y == 0) or curd != 0
##################################################
'''
