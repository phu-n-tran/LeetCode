# --------------------------------------------------------------------------
# Name:        Permuation in String
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two strings s1 and s2, write a function to return true if s2 
    contains the permutation of s1. In other words, one of the first string's
    permutations is the substring of the second string.
    
    Example 1:
        Input: s1 = "ab" s2 = "eidbaooo"
        Output: True
        Explanation: s2 contains one permutation of s1 ("ba").
    
    Example 2:
        Input:s1= "ab" s2 = "eidboaoo"
        Output: False
    
    Example 3:
        Input:s1= "abc" s2 = "ecab"
        Output: True
    
    Example 4:
        Input:s1= "abc" s2 = "ceab"
        Output: False
        
        
    Note: 
        1. The input strings only contain lower case letters.
        2. The length of both given strings is in range [1, 10,000].
        
    Hints:
        1. Obviously, brute force will result in TLE. Think of something else.
        2. How will you check whether one string is a permutation of another string?
        3. One way is to sort the string and then compare. But, Is there a 
           better way?
        4. If one string is a permutation of another string then they must one 
           common metric. What is that?
        5. Both strings must have same character frequencies, if one is permutation 
           of another. Which data structure should be used to store frequencies?
        6. What about hash table? An array of size 26?
        
     Approach used: window sliding method (slow)
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sizeS2 = len(s2)
        sizeS1 = len(s1)
        counterS1 = Counter(s1)
        
        window = None
        
        for i in range(sizeS2-sizeS1+1):
            if i == 0:
                window = Counter(s2[:sizeS1])
            else:
                window[s2[i-1]] -= 1
                window[s2[i+sizeS1-1]] += 1
            
            if len(window - counterS1) == 0:
                return True
        







        
"""other faster methods (from other submissions)
##################################################
def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        
        count_one, count_two = [0]*26, [0]*26
        for char in s1:
            count_one[ord(char) - ord('a')] += 1
        
        for i in range(n2):
            
            count_two[ord(s2[i])-ord('a')] += 1
            if i >= n1:
                count_two[ord(s2[i-n1])-ord('a')] -= 1
            
            if count_two == count_one:
                return True
        
        return False
"""
