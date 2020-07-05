# --------------------------------------------------------------------------
# Name:        Hamming Distance
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    The Hamming distance between two integers is the number of positions at
    which the corresponding bits are different.
   
    More about hamming distance: https://en.wikipedia.org/wiki/Hamming_distance

    Given two integers x and y, calculate the Hamming distance.

    Note:
      1. 0 ≤ x, y < 231.

    Example:
      Input: x = 1, y = 4
      Output: 2
      Explanation:
          1   (0 0 0 1)
          4   (0 1 0 0)
                 ↑   ↑
    The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x).replace("0b","") 
        bin_y = bin(y).replace("0b","") 
        len_x = len(bin_x)
        len_y = len(bin_y)
        count = 0
        
        if len_x > len_y:
            bin_y = "0"*(len_x-len_y) + bin_y
            
            for i in range(len_x):
                if bin_x[i] != bin_y[i]:
                    count += 1
        else:
            bin_x = "0"*(len_y-len_x) + bin_x
            
            for i in range(len_y):
                if bin_x[i] != bin_y[i]:
                    count += 1
        return count
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # s, l = min(x,y), max(x,y)
        # diff = 0
        # while s:
        #     if s%2 != l%2:
        #         diff += 1
        #     s,l = s>>1,l>>1
        # while l:
        #     if l%2 == 1:
        #         diff += 1
        #     l = l>>1
        # return diff
        return bin(x^y).count('1')
##################################################
def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x=(bin(x)[2:].zfill(32))
        y=(bin(y)[2:].zfill(32))
        cnt=0
        for i in range(len(x)):
            if x[i]!=y[i]:
                cnt+=1
        return(cnt)
        #return bin(x^y).count("1")
##################################################

'''
