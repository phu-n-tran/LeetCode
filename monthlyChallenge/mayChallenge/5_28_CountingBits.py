# --------------------------------------------------------------------------
# Name:        counting Bits (dynamic programming approach)
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non negative integer number num. For every numbers i in the 
    range 0 ≤ i ≤ num calculate the number of 1's in their binary 
    representation and return them as an array.

    Example 1:
        Input: 2
        Output: [0,1,1]
        Explain: 0 has no 1, 1 has one 1, and 2 has one 1
      
    Example 2:
        Input: 5
        Output: [0,1,1,2,1,2]
        Explain: 0 has no 1, 1 has one 1, 2 has one 1, 3 has two 1s, ...
      
    Follow up:
        1) It is very easy to come up with a solution with run time 
           O(n*sizeof(integer)). But can you do it in linear time O(n) 
           possibly in a single pass?
        2) Space complexity should be O(n).
        3) Can you do it like a boss? Do it without using any 
           builtin function like __builtin_popcount in c++ or in any other language.
           
    Hints:
        1) You should make use of what you have produced already.
        2) Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. 
           And try to generate new range from previous.
        3) Or does the odd/even status of the number help you in calculating the number of 1s?
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # this method looks at the pattern of the odd and even numbers
        result = [0 for _ in range(num+1)]
        
        for i in range(1, num+1):
            if i%2 == 0:
                result[i] = result[i//2]
            else:
                result[i] = result[i-1] + 1
        return result
        
          
            
        
 



        
"""other faster methods (from other submissions)
##################################################
# this make use of Hint #2 Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on.
# explain
# num of bits: 0  1  |  1  2  |  1   2   2   3  |  1   2   2   3   2   3
# nums:        0  1  |  2  3  |  4   5   6   7  |  8   9   10  11  12  13

def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= num:
            res += [i + 1 for i in res]
        return res[:num + 1]
"""
