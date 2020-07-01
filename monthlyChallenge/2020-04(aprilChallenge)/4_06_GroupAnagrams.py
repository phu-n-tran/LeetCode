
# --------------------------------------------------------------------------
# Name:        Group Anagrams
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of strings, group anagrams together.
    
    Example 1:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
            [
              ["ate","eat","tea"],
              ["nat","tan"],
              ["bat"]
            ]
    
    Note:
      1. All inputs will be in lowercase.
      2. The order of your output does not matter.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        elif len(strs) == 1:
            return [strs]
        
        result = {}
        
        for word in strs:
            key = tuple(sorted(word))
            result[key] = result.get(key, []) + [word]
            
        return result.values()
                    
        
        
        
        
        
        
        
        
        


"""other faster methods (from other submissions)
##################################################
def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        
        for string in strs:
            sortedstr = ''.join(sorted(string))
            if sortedstr in d:
                d[sortedstr].append(string)
            else:
                d[sortedstr] = [string]
                
        return d.values()
"""
 
