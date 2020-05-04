# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

class Solution:
    def findComplement(self, num: int) -> int:
        return num^(2**(len(bin(num)[2:]))-1)

#eg bin (5) will give '0b101' ,hence [2:] will give only 101