# Leet code problem from:
# https://leetcode.com/problems/jewels-and-stones/description/

# # You're given strings J representing the types of stones that are jewels, 
# and S representing the stones you have.  
# Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.

# # The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J, S):
        jewel_counter = 0
        jewel_dict = enumerate(J)
        for i,v in jewel_dict:
            jewel_counter += S.count(v)
        return jewel_counter
