
# --------------------------------------------------------------------------
# Name:        Sort Characters By Frequency
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string, sort it in decreasing order based on the frequency of 
    characters.
    
    Example 1:
        Input: "tree"
        Output: "eert"
        Explanation:
            'e' appears twice while 'r' and 't' both appear once.
            So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
     
    Example 2:
        Input: "cccaaa"
        Output: "cccaaa"
        Explanation:
            Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
            Note that "cacaca" is incorrect, as the same characters must be together.
    
    Example 2:
        Input: "Aabb"
        Output: "bbAa"
        Explanation:
            "bbaA" is also a valid answer, but "Aabb" is incorrect.
            Note that 'A' and 'a' are treated as two different characters.
        
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictStr = Counter(s).most_common()
        
        result = ""

        for letter, freq in dictStr:
            result += letter*freq
        
        return result
                    
                
        
        



        
"""My other slower solution
####################################################
def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        _s = set(s)
        freq = []
        for char in _s:
            freq.append((char, s.count(char)))
        
        freq.sort( key = lambda x : x[1], reverse = True)
        print(freq)
        return ''.join(map(lambda x : x[0] * x[1], freq))
"""
