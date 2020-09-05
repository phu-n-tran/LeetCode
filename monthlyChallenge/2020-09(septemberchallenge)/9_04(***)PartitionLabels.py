
# --------------------------------------------------------------------------
# Name:        Partition Labels
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    A string S of lowercase English letters is given. We want to partition
    this string into as many parts as possible so that each letter appears
    in at most one part, and return a list of integers representing the size
    of these parts.

    Example 1:
      Input: S = "ababcbacadefegdehijhklij"
      Output: [9,7,8]
      Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

    Note:
      1. S will have length in range [1, 500].
      2. S will consist of lowercase English letters ('a' to 'z') only.
    
    Hint:
     1. Try to greedily choose the smallest partition that includes the 
        first letter. If you have something like "abaccbdeffed", then you
        might need to add b. You can use an map like "last['b'] = 5" 
        to help you expand the width of your partition.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Greedy O(n) solution
        ends = {c: i for i, c in enumerate(S)}        
        curr, out = 0, [0]
        
        while curr < len(S):
            last = ends[S[curr]]
            while curr <= last:
                symb = S[curr]
                last = max(last, ends[symb])
                curr += 1
            out.append(curr)
        
        return [out[i]-out[i-1] for i in range(1, len(out))]
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        count = {}
        lastIndex = 0
        result = []
        for i in range(len(S)):
            if(S[i] not in count):
                count[S[i]] = i
                
            else:
                count[S[i]] = i
                
        maxTill = 0
                
        for i in range(len(S)):
            if(i <= maxTill):
                maxTill = max(maxTill, count[S[i]])
            else:
                maxTill = count[S[i]]
                diff = i-lastIndex
                lastIndex = i
                result.append(diff)
                
                
        diff = len(S)-lastIndex
        result.append(diff)
        
        return result
##################################################
def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        dic = defaultdict(int)
        for i,v in enumerate(S):
            dic[v] = i
        
        left = 0
        right = 0
        res = []
        
        for i,v in enumerate(S):
            right = max(right,dic[v])
            if i == right:
                res.append(right-left+1)
                left = right+1
            
        return res
##################################################
def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        mappingoflocations={}
        for i in range(len(S)):
            mappingoflocations[S[i]]=i
        start=0
        end=0
        output=[]
        while end<len(S) and start<len(S):
            tempstring=""
            end=mappingoflocations[S[start]]
            j=start
            while j<=end:
                if mappingoflocations[S[j]]>end:
                    end=mappingoflocations[S[j]]
                tempstring+=S[j]
                j+=1
            output.append(len(tempstring))
            start=end+1
        return output
##################################################
'''
