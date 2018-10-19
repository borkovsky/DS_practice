#Leet code #476
# Given a positive integer, output its complement number. 
# The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.

class Solution:
    def findComplement(self, num):
        return int(bin(num)[2:].replace('0','x').replace('1','0').replace('x','1'),2)