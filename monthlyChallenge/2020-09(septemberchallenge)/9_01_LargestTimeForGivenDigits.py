# --------------------------------------------------------------------------
# Name:        Largest Time for Given Digits
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given an array of 4 digits, return the largest 24 hour time that can be made.

    The smallest 24 hour time is 00:00, and the largest is 23:59.  
    Starting from 00:00, a time is larger if more time has elapsed since midnight.

    Return the answer as a string of length 5.  
    If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9
"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        from itertools import permutations
        import re
        
        unique = set()
        result = []
        perm = permutations(A) 
        pattern = "2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]"
  
        # Print the obtained permutations 
        for i in list(perm):
            temp = ""
            for letter in i:
                temp += str(letter)
                if len(temp) == 2:
                    temp += ":"
            unique.add(temp)
            
        for each_time in unique:
            if re.search(pattern, each_time):
                result.append(each_time)
        result.sort()
        
        if result:
            return result[-1]
        else:
            return ""
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        res = ""

        A.sort()
        
        if A[0] > 2:
            return res
        
        temp = itertools.permutations(A,4)
        res = []
    
        for x in temp:
            if x[0] < 2 and x[2] < 6:
                res.append(x)
            if x[0] == 2 and x[1] < 4 and x[2] < 6:
                res.append(x)
           
        if len(res) == 0:
            return ""
        
        y = res.pop()
        ans = "" 
        for i in y:
            ans += str(i)
            
        ans = ans[:2] + ":" + ans[2:]
        return ans
##################################################
def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        if min(A)>3:
            return ''
        max_time = None
        
        p = set(permutations(A))
        for h,i,m,j in p:
            print(h,i,m,j)
            hour = h*10+i
            minute = m*10+j
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        if max_time is None:
            return ''
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
##################################################
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        max_time = -1
        # enumerate all possibilities, with the permutation() func
        for h, i, j, k in itertools.permutations(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
##################################################
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        max_time = -1

        def build_time(permutation):
            nonlocal max_time

            h, i, j, k = permutation
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        def swap(array, i, j):
            if i != j:
                array[i], array[j] = array[j], array[i]

        def permutate(array, start):
            if start == len(array):
                build_time(array)
                return

            for index in range(start, len(array)):
                swap(array, index, start)
                # repeat the permutation with the original array mutated
                permutate(array, start+1)
                swap(array, index, start)

        permutate(A, 0)
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
'''
