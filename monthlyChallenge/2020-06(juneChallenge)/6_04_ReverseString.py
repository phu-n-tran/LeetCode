# --------------------------------------------------------------------------
# Name:        Delete Node in a Linked List
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Write a function that reverses a string. The input string is given as 
    an array of characters char[].

    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

    Example 1:
        Input: ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
  
    Example 2:
        Input: ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]
   
   Hint: The entire logic for reversing a string is based on using the 
         opposite directional two-pointer approach!
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)-2, -1, -1):
            s.append(s.pop(i))
        
                
        
        
        
 



        
'''other methods (from other submissions)
##################################################
def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):   
            s[i], s[-i - 1] = s[-i - 1], s[i]
##################################################
def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while(i < j):
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
            
        return s
'''
