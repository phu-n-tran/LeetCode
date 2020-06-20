# --------------------------------------------------------------------------
# Name:        Longest Duplicate Substring
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string S, consider all duplicated substrings: (contiguous) 
    substrings of S that occur 2 or more times. (The occurrences may overlap.)

    Return any duplicated substring that has the longest possible length.  
    (If S does not have a duplicated substring, the answer is "".)

    Example 1:
        Input: "banana"
        Output: "ana"
        
    Example 2:
        Input: "abcd"
        Output: ""


    Note:
        1. 2 <= S.length <= 10^5
        2. S consists of lowercase English letters.
    
    Hints:
        1. Binary search for the length of the answer. 
          (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
        2. To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.
        3- https://youtu.be/bwgJS7lKFSY
"""

class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        def search(m, MOD):
            h = 0
            for i in range(m):
                h = (h * 26 + nums[i]) % MOD
            s = {h}
            aL = pow(26, m, MOD)
            for pos in range(1, n - m + 1):
                h = (h * 26 - nums[pos - 1] * aL + nums[pos + m - 1]) % MOD
                if h in s:
                    return pos
                s.add(h)
            return -1

        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        l, r = 1, n
        pos = -1
        MOD = 2**63 - 1
        while l <= r:
            m = (l + r) // 2
            cur = search(m, MOD)
            if cur != -1:
                l = m + 1
                pos = cur
            else:
                r = m - 1
        return S[pos: pos + l - 1]

    
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def search(L, a, mod, nums):
            h = 0
            for i in range(L):
                h = (h * a + nums[i]) % mod
                
            seen = {h:0}
            aL = pow(a, L, mod)
            for start in range(1, n - L + 1):
                h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % mod
                if h in seen:
                    if nums[seen[h]:seen[h] + L] == nums[start:start + L]:
                        return start
                seen[h] = start
            return -1
        
        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        a, mod = 26, 10 ** 9 + 7
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if search(mid, a, mod, nums) != -1:
                l = mid + 1
            else:
                r = mid - 1
        start = search(l - 1, a, mod, nums)
        return S[start:start + l - 1]
'''
