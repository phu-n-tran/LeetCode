# --------------------------------------------------------------------------
# Name:        Numbers With Same Consecutive Differences
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Return all non-negative integers of length N such that the absolute 
    difference between every two consecutive digits is K.

    Note that every number in the answer must not have leading zeros except
    for the number 0 itself. For example, 01 has one leading zero and is 
    invalid, but 0 is valid.

    You may return the answer in any order.

    Example 1:
      Input: N = 3, K = 7
      Output: [181,292,707,818,929]
      Explanation: Note that 070 is not a valid number, because it has leading zeroes.
    
    Example 2:
      Input: N = 2, K = 1
      Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


    Note:
      1. 1 <= N <= 9
      2. 0 <= K <= 9
      
    Leet Solution: https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution/
"""


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N <= 0:
            return []
        if N == 1:
            return list(range(10))
        i = 1
        q = collections.deque([1,2,3,4,5,6,7,8,9])
        while i < N:
            for _ in range(len(q)):
                n = q.popleft()
                m = n % 10
                if 0 <= m-K <= 9:
                    q.append(n*10+m-K)
                if 0 <= m+K <= 9 and m+K != m-K:
                    q.append(n*10+m+K)
            i += 1
            if i == N:
                return q
        return q
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def numsSameConsecDiff(self, N, K):
        ans = {x for x in range(1, 10)}
        for _ in xrange(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
##################################################
def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1: return set(range(0,10))
        nums = set(range(1, 10))
        output = set()
        for i in range(N-1):
            newSet = set()
            for num in nums:
                last = num%10
                if last + K <=9: newSet.add(10*num + (last+K))
                if last-K>=0: newSet.add(10*num + (last-K))
            nums = newSet
        return list(nums)
##################################################
def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        answers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for i in range(N-1):
            newAnswers = []
            for ans in answers:
                lastDigit = ans % 10
                if ans >= 0 and lastDigit + K < 10:
                    newAnswer = ans * 10 + lastDigit + K
                    newAnswers.append(newAnswer)
                if ans >= 0 and K > 0 and lastDigit - K >= 0:
                    newAnswer = ans * 10 + lastDigit - K
                    newAnswers.append(newAnswer)
            answers = newAnswers
        answers = [x for x in answers if len(str(x)) == N]
        return answers
'''
