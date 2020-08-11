# --------------------------------------------------------------------------
# Name:        H-Index
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of citations (each citation is a non-negative integer) 
    of a researcher, write a function to compute the researcher's h-index.

    According to the definition of h-index on Wikipedia: "A scientist has
    index h if h of his/her N papers have at least h citations each, and 
    the other N − h papers have no more than h citations each."

    Example:
      Input: citations = [3,0,6,1,5]
      Output: 3 
      Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
                   received 3, 0, 6, 1, 5 citations respectively. 
                   Since the researcher has 3 papers with at least 3 citations each and the remaining 
                   two with no more than 3 citations each, her h-index is 3.
    
    Note: If there are several possible values for h, the maximum one is taken as the h-index.
    
    Hints:
      1. An easy approach is to sort the array first.
      2. What are the possible values of h-index?
      3. A faster approach is to use extra space.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        bucket = [0] * (len(citations) + 1)
        
        for i in range(len(citations)):
            if citations[i] > len(citations):
                bucket[len(citations)] += 1
            else:
                bucket[citations[i]] += 1
                
        count = 0
        for i in range(len(bucket) - 1, -1, -1):
            count += bucket[i]
            if count >= i:  #  If the value of count is greater than the index value then we return the index
                return i
        
        return 0  # If no such index is found then we simply return 0

                
        
        
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # target: find the first index which make citations[i] >= len(citations) - i
        return self.first(citations)
        
    
    def first(self, citations):
        citations.sort()
        for i, num in enumerate(citations):
            if num >= len(citations) - i:
                return len(citations) - i
        return 0
##################################################
def hIndex(self, citations):
        N = len(citations)
        citations.sort()
        i = 0
        while i < N and citations[N - 1 - i] > i:
            i += 1
        return i
##################################################
def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """


        citations.sort()


        list_len = len(citations)
        for i in range(list_len):
            num = citations[i]
            ok = list_len-i
            if num >= ok:
                return ok
        return 0
##################################################
def hIndex(self, citations):
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
'''
