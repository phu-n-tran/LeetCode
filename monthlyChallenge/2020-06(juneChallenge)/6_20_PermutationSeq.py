# --------------------------------------------------------------------------
# Name:        Permutation Sequence
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    The set [1,2,3,...,n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the 
    following sequence for n = 3:
        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
    Given n and k, return the kth permutation sequence.

    Note:
        1. Given n will be between 1 and 9 inclusive.
        2. Given k will be between 1 and n! inclusive.
    
    Example 1:
        Input: n = 3, k = 3
        Output: "213"
        
    Example 2:
        Input: n = 4, k = 9
        Output: "2314"
"""

from itertools import permutations 
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        plist = [i for i in range(1, n+1)]
        
        temp_result = list(permutations(plist, n))[k-1]
        
        result = ""
        for i in temp_result:
            result += str(i)
        
        return result
    
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lst = range(1, n+1)
        k -= 1
        ans = ""
        while n > 0:
            idx, k = divmod(k, math.factorial(n-1))
            ans += str(lst[idx])
            lst.remove(lst[idx])
            n -= 1
        
        return ans
##################################################
def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.helper(n, k, [i for i in range(1, n+1)])
    
    def helper(self, n, k, sortl):
        if n == 1:
            return str(sortl[k-1])
        else:
            choices = 1
            # A(len(sortl)-1, n-1)
            for i in range(len(sortl)-1, len(sortl)-n, -1):
                choices*=i
            # print(choices)
            idx = (k-1)//choices
            first = sortl[idx]
            # print(n-1, k-idx*choices, sortl[:idx] + sortl[idx+1:])
            ans = str(first) + self.helper(n-1, k-idx*choices, sortl[:idx] + sortl[idx+1:])
            return ans
'''
