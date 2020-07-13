# --------------------------------------------------------------------------
# Name:        Reverse Bits
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Reverse bits of a given 32 bits unsigned integer.

    Example 1:
      Input: 00000010100101000001111010011100
      Output: 00111001011110000010100101000000
      Explanation: The input binary string 00000010100101000001111010011100 
                   represents the unsigned integer 43261596, so return 964176192
                   which its binary representation is 00111001011110000010100101000000.
    
    Example 2:
      Input: 11111111111111111111111111111101
      Output: 10111111111111111111111111111111
      Explanation: The input binary string 11111111111111111111111111111101
                   represents the unsigned integer 4294967293, so return 3221225471
                   which its binary representation is 10111111111111111111111111111111.


    Note:
      1. Note that in some languages such as Java, there is no unsigned integer type.
         In this case, both input and output will be given as signed integer type and
         should not affect your implementation, as the internal binary representation
         of the integer is the same whether it is signed or unsigned.
      2. In Java, the compiler represents the signed integers using 2's complement 
         notation. Therefore, in Example 2 above the input represents the signed integer 
         -3 and the output represents the signed integer -1073741825.

    Follow up:
      If this function is called many times, how would you optimize it?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out
        
            
        
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def reverseBits(self, n):
        res = 0 
        for _ in xrange(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res
##################################################
def reverseBits(self, n):
        ## sol1
        # ans = bin(n)
        # return int(ans[:2] + ans[2:].zfill(32)[::-1], 2)

        ## sol2
        res = 0
        for i in range(32):
            res <<= 1
            res |= ((n >> i) & 1)
        return res
##################################################
def reverseBits(self, n):
        print(n)
        bin_n = '{:032b}'.format(n)
        #bin_n = bin(n)
        print(bin_n)
        reverse = "0b"
        
        for i in range(31, -1 ,-1):
            reverse+=bin_n[i]
        return int(reverse, 2)
'''
