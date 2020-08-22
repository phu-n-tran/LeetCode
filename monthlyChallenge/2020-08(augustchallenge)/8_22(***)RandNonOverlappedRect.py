
# --------------------------------------------------------------------------
# Name:        Random Point in Non-overlapping Rectangles
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a list of non-overlapping axis-aligned rectangles rects, write a
    function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

    Note:
      An integer point is a point that has integer coordinates. 
      A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
      ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer 
      coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
      length and width of each rectangle does not exceed 2000.
      1 <= rects.length <= 100
      pick return a point as an array of integer coordinates [p_x, p_y]
      pick is called at most 10000 times.
    
    Example 1:
      Input: 
        ["Solution","pick","pick","pick"]
        [[[[1,1,5,5]]],[],[],[]]
      Output: 
        [null,[4,1],[4,1],[3,3]]
   
    Example 2:
      Input: 
        ["Solution","pick","pick","pick","pick","pick"]
        [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
      Output: 
        [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
      Explanation of Input Syntax:
        The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""



class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.ranges = ranges = [0]
        self.rects = rects
        for x1,y1,x2,y2 in rects:
            ranges.append( ranges[-1] + (y2-y1+1)*(x2-x1+1) )

    def pick(self):
        """
        :rtype: List[int]
        """
        ranges, rects = self.ranges, self.rects
        areaPt = random.randint(1,ranges[-1])
        x1,y1,x2,y2 = rects[bisect.bisect_left(ranges,areaPt)-1]
        return [random.randint(x1,x2), random.randint(y1,y2)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        points = [0]
        self.rects = []
        for rect in rects:
            [x1, y1, x2, y2] = rect
            M, N = (x2-x1+1), (y2-y1+1)
            points.append(M*N + points[-1])
            self.rects.append((x1,y1,N))
        
        self.points = points

    def pick(self):
        """
        :rtype: List[int]
        """
        point = randrange(self.points[-1])
        rec = bisect.bisect_left(self.points, point)
        if point != self.points[rec]: rec -= 1
            
        x, y, N = self.rects[rec]
        point -= self.points[rec]
        
        return [x+point/N, y+point%N]
##################################################
import bisect
class Solution(object):
    
    
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.weight = [0]
        self.sumVal = 0
        for ele in self.rects:
            self.sumVal+=((ele[3]-ele[1]+1)*(ele[2]-ele[0]+1))
            self.weight.append(self.sumVal)

        

    def pick(self):
        """
        :rtype: List[int]
        """
        rand = random.randint(0,self.sumVal-1)
        ind = bisect.bisect_right(self.weight,rand)

        

        rand-=self.weight[ind-1]

        return [self.rects[ind-1][0]+rand % ( self.rects[ind-1][2]- self.rects[ind-1][0]+1),self.rects[ind-1][1]+rand / ( self.rects[ind-1][2]- self.rects[ind-1][0]+1)]
##################################################
'''
