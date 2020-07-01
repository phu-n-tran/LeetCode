# --------------------------------------------------------------------------
# Name:        Remove K Digits
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Given a non-negative integer num represented as a string, remove k 
    digits from the number so that the new number is the smallest possible.
    
    Example 1:
        Input: num = "1432219", k = 3
        Output: "1219"
        Explanation: Remove the three digits 4, 3, and 2 to form the new 
                     number 1219 which is the smallest.
    
    Example 2:
        Input: num = "10200", k = 1
        Output: "200"
        Explanation: Remove the leading 1 and the number is 200. Note that
                     the output must not contain leading zeroes.
    
    Example 3:
        Input: num = "10", k = 2
        Output: "0"
        Explanation: Remove all the digits from the number and it is left
                     with nothing which is 0.
    
    Note:
        1) The length of num is less than 10002 and will be ≥ k.
        2) The given num does not contain any leading zero.
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        
        result = list(num)
        
        # check k times, remove the current number that less than
        # the next number (start from left to right)
        for j in range(k):
            i = 0
            while i < len(result)-1 and result[i] <= result[i+1]:
                i += 1
            result.pop(i)
        
        result = "".join(result).lstrip("0")

        if result == "":
            return "0"
        else:
            return result







        
""" faster methods (from other submissions)
##################################################
def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not num or k is None:
            return ''
        
        if k >= len(num):
            return '0'
        
        stack = []
        
        for n in num:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        return str(int(''.join(map(str, stack))))
 #########################################################
 def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        i=0
        j=k
        z=-1
        while i<len(num) and (j>0 or num[i]=='0') :
            
            if num[i]=='0':
                z=i
                i+=1
                
            else:
                i+=1
                j-=1
        
        chose=i-z-1
        left=num[z+1:]
        #print i,j,z
        def helper(l,c):
            it=0;itn=1
            while c>0 and it<len(l):
                #print l,it,itn,l[it],l[itn]
                if itn==len(l):
                    l[it]="*"
                    it-=1
                    c-=1
                elif it==-1:
                    it=itn
                elif l[it]=="*":
                    it-=1
                elif  l[it]>l[itn]:
                    l[it]= '*'
                    it-=1
                    c-=1
                elif  l[it]<=l[itn]:
                    it=itn
                    itn+=1
                else:
                    it+=1
                    itn+=1
            return l
        res = "".join(helper(list(left),chose)).replace("*","").lstrip("0")
        if not res  :
            return "0"
        else:
            return res
"""
