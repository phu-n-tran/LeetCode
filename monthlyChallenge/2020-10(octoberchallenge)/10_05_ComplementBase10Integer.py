
# --------------------------------------------------------------------------
# Name:        Complement of Base 10 Integer
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Every non-negative integer N has a binary representation.  
    For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on. 
    Note that except for N = 0, there are no leading zeroes in any binary representation.

    The complement of a binary representation is the number in binary you get 
    when changing every 1 to a 0 and 0 to a 1.  For example, the complement 
    of "101" in binary is "010" in binary.

    For a given number N in base-10, return the complement of it's binary 
    representation as a base-10 integer.


    Example 1:
      Input: 5
      Output: 2
      Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
    
    Example 2:
      Input: 7
      Output: 0
      Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
    
    Example 3:
      Input: 10
      Output: 5
      Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 
    Note:
      1. 0 <= N < 10^9
      2. This question is the same as 476: https://leetcode.com/problems/number-complement/
    
    Hints:
      1. A binary number plus its complement will equal 111....111 in binary. Also, N = 0 is a corner case.
"""


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_N = bin(N).replace("0b", "")
        result = ""
        for bit in bin_N:
            if bit == "0":
                result += "1"
            else:
                result += "0"
        # print(bin_N)
        # print(result)
        return int(result, 2)
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        bit_n = '{:b}'.format(N)
        complement = "".join(['1' if c == '0' else '0' for c in bit_n])
        return int(complement, 2)
##################################################
def bitwiseComplement(self, N):
        formatBinary = format(N, 'b')

        stringBinary = str(formatBinary)

        charArray = []
        for char in stringBinary:
            charArray.append(char)

        complementArray = []
        for char in charArray:
            if char == '0':
                complementArray.append('1')
            else:
                complementArray.append('0')

        complementStr = ''.join(complementArray)
        sol = int(complementStr, 2)
        return(sol)
##################################################
def bitwiseComplement(self, N):
        if N == 1:
            return 0
        if N == 0:
            return 1
        
        M = 2
        while M <= N:
            M = M << 1
            
        return abs(M - N - 1)
##################################################
'''
