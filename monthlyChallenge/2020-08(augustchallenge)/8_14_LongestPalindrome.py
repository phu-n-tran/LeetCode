# --------------------------------------------------------------------------
# Name:        Longest Palindrome
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a string which consists of lowercase or uppercase letters, find the
    length of the longest palindromes that can be built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.

    Note:
    Assume the length of given string will not exceed 1,010.

    Example:
      Input:
        "abccccdd"
      Output:
        7

    Explanation:
      One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        countDict = dict()
        onceFlag = True # use to count odd once
        longestLength = 0
        for letter in s:
            countDict[letter] = countDict.get(letter, 0) + 1
        
        for val in countDict.values():
            # if even numver of letter
            if val % 2 == 0:
                longestLength += val
            else: # if odd number of letter
                if onceFlag: 
                    longestLength += val
                    onceFlag = False
                else:
                    longestLength += val - 1
                    
        return longestLength
                
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        flag=0
        c={}
        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for key, value in c.items():
            if value%2==0:
                result+=value
            else:
                flag=1
                if value>1:
                    result+=(value-1)
        if flag==0:
            return result
        else:
            return result+1
##################################################
def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        count = 0
        for key in dic.keys():
            val = dic[key]
            count += val // 2 * 2
            
            if val % 2 == 1 and count % 2 == 0:
                count += 1
        
        return count
##################################################
def longestPalindrome(self, s):
        """
        - all evenly occuring will contribute
        - from oddly occuring, we just need one
        """
        dist = set()
        for item in s:
            if item not in dist:
                dist.add(item)
            else:
                dist.remove(item)
        return len(s) - len(dist) + 1 if len(dist) else len(s)
'''
