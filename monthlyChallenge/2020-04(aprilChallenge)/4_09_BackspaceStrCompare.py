
# --------------------------------------------------------------------------
# Name:        Backspace String Compare
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two strings S and T, return if they are equal when both are typed
    into empty text editors. # means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.
    
    Example 1:
        Input: S = "ab#c", T = "ad#c"
        Output: true
        Explanation: Both S and T become "ac".
    
    Example 2:
        Input: S = "ab##", T = "c#d#"
        Output: true
        Explanation: Both S and T become "".
    
    Example 3:
        Input: S = "a##c", T = "#a#c"
        Output: true
        Explanation: Both S and T become "c".
    
    Example 4:
        Input: S = "a#c", T = "b"
        Output: false
        Explanation: S becomes "c" while T becomes "b".
    
    Note:
      1. 1 <= S.length <= 200
      2. 1 <= T.length <= 200
      3. S and T only contain lowercase letters and '#' characters.
    
    Follow up: Can you solve it in O(N) time and O(1) space?
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        list_s = []
        list_t = []
        
        for letter in S:
            if letter == "#" and list_s:
                list_s.pop()
            elif letter != "#":
                list_s.append(letter)
                
        for letter in T:
            if letter == "#" and list_t:
                list_t.pop()
            elif letter != "#":
                list_t.append(letter)
                
        return list_s == list_t
        
                    
        
        
        
        
        
        
        
        
        


"""other faster methods (from other submissions)
##################################################
def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for i in S:
            if i!= '#':
                stack1.append(i)
            elif len(stack1) > 0:
                stack1.pop()
        
        for i in T:
            if i!= '#':
                stack2.append(i)
            elif len(stack2) > 0:
                stack2.pop()
        if len(stack1) != len(stack2):
            return False
        
        for i in range(len(stack1)):
            if stack1[i] != stack2[i]:
                return False
        return True
"""
