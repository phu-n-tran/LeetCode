# --------------------------------------------------------------------------
# Name:        Find All Anagrams in a String
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string s and a non-empty string p, find all the start indices
    of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of 
    both strings s and p will not be larger than 20,100.

    The order of output does not matter.
    
    Example 1:
        Input:
            s: "cbaebabacd" p: "abc"
        Output:
            [0, 6]
        Explanation:
            The substring with start index = 0 is "cba", which is an anagram of "abc".
            The substring with start index = 6 is "bac", which is an anagram of "abc".
    
    Example 2:
        Input:
            s: "abab" p: "ab"
        Output:
            [0, 1, 2]
        Explanation:
            The substring with start index = 0 is "ab", which is an anagram of "ab".
            The substring with start index = 1 is "ba", which is an anagram of "ab".
            The substring with start index = 2 is "ab", which is an anagram of "ab".
            
    For this one, I use the Window Sliding Technique + hashabel 
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counterP = Counter(p)
        sizeP = len(p)
        sizeS = len(s)
        result = []
        
        window = None
        
        for i in range(sizeS-sizeP+1):
            if i == 0:
                window = Counter(s[:sizeP])
            else:
                window[s[i-1]] -= 1
                window[s[i+sizeP-1]] += 1
            
            if len(counterP - window) == 0:
                result.append(i)
                    
        return result








        
"""other faster methods (from other submissions)
##################################################
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d = dict()
        l = []
        for c in p:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        temp = dict(d)
        cont = False
        j=-1
        for i,c in enumerate(s):
            if c in temp:
                if j==-1:
                    j = i
                cont= True
                temp[c]-=1
                if temp[c] == 0:
                    temp.pop(c)
                if len(temp) == 0:
                    l.append(j)
                    temp[s[j]]=1
                    j+=1
            elif cont:
                if c not in d:
                    temp = dict(d)
                    cont = False
                    j = -1
                else:
                    while s[j] != c and j<i:
                        if s[j] in temp:
                            temp[s[j]] += 1
                        else:
                            temp[s[j]] = 1
                        j+=1
                    if s[j] == c and j<i:
                        j+=1                                                            
                #print(j,temp)                               
        
        return l
############################################
def findAnagrams(self, s, p):
        checker = [0] * 26
        for word in p:
            checker[ord(word)-97]+=1
        
        checker2 = [0] * 26
        i = 0
        j = len(p)
        ans = []
        for word in s:
            if i<j-1:
                checker2[ord(word)-97]+=1
            else:
                checker2[ord(word)-97]+=1
                if checker == checker2:
                    ans.append(i-j+1)
                
                checker2[ord(s[i-j+1])-97]-=1
               
            i = i + 1
            
        return ans
"""
