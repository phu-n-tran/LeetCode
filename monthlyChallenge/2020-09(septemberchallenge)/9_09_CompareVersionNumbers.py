# --------------------------------------------------------------------------
# Name:        Compare Version Numbers
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Compare two version numbers version1 and version2.
    If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.

    The . character does not represent a decimal point and is used to separate number sequences.

    For instance, 2.5 is not "two and a half" or "half way to version three", 
    it is the fifth second-level revision of the second first-level revision.

    You may assume the default revision number for each level of a version number 
    to be 0. For example, version number 3.4 has a revision number of 3 and 4 for 
    its first and second level revision number. Its third and fourth level revision number are both 0.


    Example 1:
      Input: version1 = "0.1", version2 = "1.1"
      Output: -1
    
    Example 2:
      Input: version1 = "1.0.1", version2 = "1"
      Output: 1
    
    Example 3:
      Input: version1 = "7.5.2.4", version2 = "7.5.3"
      Output: -1
    
    Example 4:
      Input: version1 = "1.01", version2 = "1.001"
      Output: 0
      Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
    
    Example 5:
      Input: version1 = "1.0", version2 = "1.0.0"
      Output: 0
      Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"

    Note:
      1. Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
      2. Version strings do not start or end with dots, and they will not be two consecutive dots.
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
        v1 = version1.split(".")
        v2 = version2.split(".")
        s1 = len(v1)
        s2 = len(v2)
        
        i = 0
        
        while i < s1 and i < s2:
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
            
            i += 1
        
        if s1 > s2:
            for k in range(i, s1):
                if int(v1[k]) != 0:
                    return 1
        else:
            for k in range(i, s2):
                if int(v2[k]) != 0:
                    return -1
        return 0
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = [int(i) for i in version1.split('.')]
        l2 = [int(i) for i in version2.split('.')]
        i = len(l2) - 1
        while i >= 0:
            if l2[i]:
                break
            l2 = l2[:-1]
            i -= 1
        i = len(l1) - 1
        while i >= 0:
            if l1[i]:
                break
            l1 = l1[:-1]
            i -= 1
        for i in range(min(len(l2), len(l1))):
            if l1[i] < l2[i]:
                return -1
            elif l2[i] < l1[i]:
                return 1
        
        if len(l1) > len(l2):
            return 1
        elif len(l2) > len(l1):
            return -1
        return 0
##################################################
def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        while len(v1) != len(v2):
            if len(v1)<len(v2):
                v1.append(0)
            else :
                v2.append(0)
        
        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        
        return 0
##################################################
def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split('.')
        b = version2.split('.')
        i = 0
        while i < len(a) or i < len(b):
            x = 0 if i >= len(a) else int(a[i])
            y = 0 if i >= len(b) else int(b[i])
            if x < y:
                return -1
            elif x > y:
                return 1
            i += 1
        return 0
##################################################
'''
