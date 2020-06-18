# --------------------------------------------------------------------------
# Name:        H-Index II
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of citations sorted in ascending order (each citation is 
    a non-negative integer) of a researcher, write a function to compute the
    researcher's h-index.

    According to the definition of h-index on Wikipedia: "A scientist has 
    index h if h of his/her N papers have at least h citations each, and the
    other N − h papers have no more than h citations each."

    Example:
        Input: citations = [0,1,3,5,6]
        Output: 3 
        Explanation: [0,1,3,5,6] means the researcher has 5 papers in total 
                     and each of them had received 0, 1, 3, 5, 6 citations 
                     respectively. Since the researcher has 3 papers with at 
                     least 3 citations each and the remaining two with no more
                     than 3 citations each, her h-index is 3.
    Note:
        If there are several possible values for h, the maximum one is taken 
        as the h-index.

    Follow up:
        1. This is a follow up problem to H-Index, where citations is now guaranteed 
           to be sorted in ascending order.
        2. Could you solve it in logarithmic time complexity?
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        res=0
        for i in range(l):
            if citations[l-i-1]>=(res+1):res+=1
            else:return res
        return res

    
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    if n == 0: 
        return 0
    #citations.sort(reverse = True)
    for i in range(n):
        if citations[n - 1 - i] <= i:
            return i
    return n
'''
