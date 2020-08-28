# --------------------------------------------------------------------------
# Name:        Implement Rand10() Using Rand7()
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a function rand7 which generates a uniform random integer in the 
    range 1 to 7, write a function rand10 which generates a uniform random
    integer in the range 1 to 10.

    Do NOT use system's Math.random(). 

    Example 1:
      Input: 1
      Output: [7]

    Example 2:
      Input: 2
      Output: [8,4]

    Example 3:
      Input: 3
      Output: [8,1,10]

    Note:
      1. rand7 is predefined.
      2. Each testcase has one argument: n, the number of times that rand10 is called.

    Follow up:
      1. What is the expected value for the number of calls to rand7() function?
      2. Could you minimize the number of calls to rand7()?
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        # not uniformlly distributed
        # return ((rand7() + rand7()) % 10) + 1
        x=rand7()
        if x<6:
            t=rand7()
            while t==7: t=rand7()
        else:
            t=x
            while x>5: x=rand7()
        return 2*x-t%2
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def rand10(self):
        """
        :rtype: int
        """
        return random.randint(1, 10)
##################################################
def rand10(self):
        """
        :rtype: int
        """
        while True:
            a, b = rand7(), rand7()
            num = a + (b-1)*7
            if num>40:
                continue
            else:
                return num % 10 + 1
##################################################

'''
