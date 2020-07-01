# --------------------------------------------------------------------------
# Name:        Validate IP address
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    Write a function to check whether an input string is a valid 
    IPv4 address or IPv6 address or neither.

    IPv4 addresses are canonically represented in dot-decimal notation, 
    which consists of four decimal numbers, each ranging from 0 to 255, 
    separated by dots ("."), e.g.,172.16.254.1;

    Besides, leading zeros in the IPv4 is invalid. For example, the address 
    172.16.254.01 is invalid.

    IPv6 addresses are represented as eight groups of four hexadecimal digits,
    each group representing 16 bits. The groups are separated by colons (":").
    For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid
    one. Also, we could omit some leading zeros among four hexadecimal digits 
    and some low-case characters in the address to upper-case ones, so 
    2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
    (Omit leading zeros and using upper cases).

    However, we don't replace a consecutive group of zero value with a single
    empty group using two consecutive colons (::) to pursue simplicity. 
    For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

    Besides, extra leading zeros in the IPv6 is also invalid. For example, the
    address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

    Note: You may assume there is no extra space or special characters in the input string.

    Example 1:
        Input: "172.16.254.1"
        Output: "IPv4"
        Explanation: This is a valid IPv4 address, return "IPv4".
        
    Example 2:
        Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
        Output: "IPv6"
        Explanation: This is a valid IPv6 address, return "IPv6".
        
    Example 3:
        Input: "256.256.256.256"
        Output: "Neither"
        Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

import re
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        if re.search("^((1)\d\d|25[0-5]|2[0-4]\d|[1-9]\d|\d)\.((1)\d\d|25[0-5]|2[0-4]\d|[1-9]\d|\d)\.((1)\d\d|25[0-5]|2[0-4]\d|[1-9]\d|\d)\.((1)\d\d|25[0-5]|2[0-4]\d|[1-9]\d|\d)$", IP):
            return "IPv4"
        elif re.search("^[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}$", IP):
            return "IPv6"
        else:
            return "Neither"
    
        
        
        
        
            
    


        
'''other methods (from other submissions)
##################################################
def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def isIPv4(inputStr):
            # groups sep by '.'
            splitInput = inputStr.split('.') 
            if len(splitInput) != 4:
                return False
				
            for group in splitInput:
                if len(group) == 0:
                    return False
                if group[0] == '0' and len(group) > 1: 
                    return False
					
                if not group.isdigit() or int(group) < 0 or int(group) > 255:
                    return False
					
            return True
        
        def isIPv6(inputStr):
            splitInput = inputStr.split(':') 
			
            if len(splitInput) != 8:
                return False
            
            for group in splitInput:
                if len(group) > 4 or len(group) < 1: 
                    return False
                for char in group:
                    if char not in string.hexdigits:
                        return False
            return True
                
        if isIPv4(IP):
            return 'IPv4'
        if isIPv6(IP):
            return 'IPv6'
        return 'Neither'
##################################################
import re
class Solution(object):
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile('^(' + chunk_IPv4 + '\.){3}' + chunk_IPv4 + '$' )
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile('^(' + chunk_IPv6 + '\:){7}' + chunk_IPv6 + '$')

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 
##################################################
from ipaddress import ip_address, IPv6Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"
'''
