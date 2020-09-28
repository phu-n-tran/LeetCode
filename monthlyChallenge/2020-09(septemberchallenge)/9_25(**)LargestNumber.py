# --------------------------------------------------------------------------
# Name:        Largest Number
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a list of non negative integers, arrange them such that they form the largest number.

    Example 1:
        Input: [10,2]
        Output: "210"
    
    Example 2:
        Input: [3,30,34,5,9]
        Output: "9534330"
        
    Note: The result may be very large, so you need to return a string instead of an integer.
"""


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

                
            
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other methods (from other submissions)
##################################################
def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
        nums=map(str,nums)
        nums.sort(cmp=comp,reverse=True)
        return str(int("".join(nums)))
##################################################
def largestNumber(self, nums):
        if not any(nums):
            return "0"
        nums = map(str, nums)
        
        return "".join(sorted(nums, cmp=lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0)))
##################################################
def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        tmp = {}
        for i in nums:
            k = str(i)
            if len(k) not in tmp:
                tmp[len(k)] = []
            tmp[len(k)].append(i)
        for i in tmp:
            tmp[i].sort(reverse=True)
        tmp = tmp.values()
        while(len(tmp) != 1):
            x = tmp.pop()
            y = tmp.pop()
            tmp1 = []
            i = 0
            j = 0
            while(i < len(x) and j < len(y)):
                t = str(x[i]) + str(y[j])
                t1 = str(y[j]) + str(x[i])
                if t > t1:
                    tmp1.append(x[i])
                    i += 1
                elif t1 > t:
                    tmp1.append(y[j])
                    j += 1
                elif t1 == t:
                    tmp1.append(x[i])
                    tmp1.append(y[j])
                    i += 1
                    j += 1
            while(i < len(x)):
                tmp1.append(x[i])
                i += 1
            while(j < len(y)):
                tmp1.append(y[j])
                j += 1
            tmp.append(tmp1)
        result = ""
        number_other_than_zero = False
        for i in tmp[0]:
            if i > 0:
                number_other_than_zero = True
            result += str(i)
        if not number_other_than_zero:
            return "0"
        return result
##################################################
'''
