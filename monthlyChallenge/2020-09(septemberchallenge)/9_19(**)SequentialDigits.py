# --------------------------------------------------------------------------
# Name:        Sequential Digits
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    An integer has sequential digits if and only if each digit in the number 
    is one more than the previous digit.

    Return a sorted list of all the integers in the range [low, high] 
    inclusive that have sequential digits.

    Example 1:
      Input: low = 100, high = 300
      Output: [123,234]

    Example 2:
      Input: low = 1000, high = 13000
      Output: [1234,2345,3456,4567,5678,6789,12345]


    Constraints:
      1. 10 <= low <= high <= 10^9
    
    Hints:
      1. Generate all numbers with sequential digits and check if they are in the given range.
      2. Fix the starting digit then do a recursion that tries to append all valid digits.
"""


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return out
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return out
##################################################
def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        start = len(str(low))
        end = len(str(high))
        ans = []
        
        for d in range(start, end + 1):
            for i in range(1, 11 - d):
                num = ""
                for k in range(d):
                    num += str(i+k)
                if low <= int(num) <= high:
                    ans.append(int(num))
        
        return ans
##################################################
def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums
##################################################
'''
