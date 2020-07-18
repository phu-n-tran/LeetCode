# --------------------------------------------------------------------------
# Name:        Top K Frequent Elements
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-empty array of integers, return the k most frequent elements.

    Example 1:
      Input: nums = [1,1,1,2,2,3], k = 2
      Output: [1,2]
    
    Example 2:
      Input: nums = [1], k = 1
      Output: [1]
    
    Note:
      1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
      2. Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
      3. It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
      4. You can return the answer in any order.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countDict = {}
        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1
        
        return sorted(countDict, key=lambda x: countDict[x], reverse=True)[:k]

            
        
                
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other  methods (from other submissions)
##################################################
import heapq
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(heap)
        
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
##################################################
def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        d = {}
        output = []
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        dmap = sorted(d, key=d.get)
        f_dmap = dmap[::-1]
        
        for i in range(k):
            output.append(f_dmap[i])
            
        
        return output
##################################################
def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap={}
        for val in nums:
            if val in hashmap:
                hashmap[val]+=1
            else:
                hashmap[val]=1
        temp=[i for i,v in sorted(hashmap.items(), key=lambda x:x[1],reverse=True)]
        return [temp[i] for i in range(k)]
'''
