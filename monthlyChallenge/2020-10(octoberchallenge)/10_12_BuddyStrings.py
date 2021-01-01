# --------------------------------------------------------------------------
# Name:        Buddy Strings
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given two strings A and B of lowercase letters, return true if you can
    swap two letters in A so the result is equal to B, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) 
    such that i != j and swapping the characters at A[i] and A[j]. 
    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


    Example 1:
      Input: A = "ab", B = "ba"
      Output: true
      Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
    
    Example 2:
      Input: A = "ab", B = "ab"
      Output: false
      Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

    Example 3:
      Input: A = "aa", B = "aa"
      Output: true
      Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
    
    Example 4:
      Input: A = "aaaaaaabc", B = "aaaaaaacb"
      Output: true
    
    Example 5:
      Input: A = "", B = "aa"
      Output: false

    Example 6:
      Input: A = "acb", B = "bac"
      Output: false

    Constraints:
      1) 0 <= A.length <= 20000
      2) 0 <= B.length <= 20000
      3) A and B consist of lowercase letters.
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # False if A has different length than B
        if len(A) != len(B):
            return False
        
        # if A and B have the same string
        if A == B:
            if len(A) <= 1: # false if their length is 1 or less
                return False
            else: # if length is 2 or more
                count_dict = {}
                for a_val in A:
                    if count_dict.get(a_val, 0) == 1: # check if it is swapable - there are two same letters
                        return True
                    
                    count_dict[a_val] = 1
        else: # if A and B are not the same string
            count_diff = 0
            track_diff = [] # list of tuple (a, b)
            for i in range(len(A)): # keep track of the diff of A and B per position
                if A[i] != B[i]:
                    count_diff += 1
                    track_diff.append((A[i], B[i]))
                
                if count_diff > 2: # false if there are more than 2 positions
                    return False
            if count_diff == 2: # if there are exactly 2 differences
                # expect [(a1, b1), (a2, b2)] where a1 == b2 and b1 == a2
                if track_diff[0][0] == track_diff[1][1] and track_diff[0][1] == track_diff[1][0]: 
                    return True
        return False
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            
            freq = defaultdict(int)
            for c in A:
                freq[c] += 1
            for key, count in freq.items():
                if count > 1:
                    return True
            return False
            
        # A != B
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
        return len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]
##################################################
def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if len(A)!=len(B):
            return False
    
        mismatch=list()
        for i in range(0,len(A)):
            
            if len(mismatch) > 2:
                return False
            
            if A[i] != B[i]:
                mismatch.append((A[i],B[i]))
            
            
        if len(mismatch) == 2:
            return mismatch[0] == mismatch[1][::-1]
            
        if len(mismatch) == 0:
            return len(A) - len(set(A)) != 0
              
        return False 
##################################################
##################################################
'''
