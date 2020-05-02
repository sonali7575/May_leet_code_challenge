# Jewels and Stones
#
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  ' \
#  'Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a"
# is considered a different type of stone from "A".
# eg :
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # As J is said to be unique, dictionary can be used and S can be iterated and checked if stones are present in the
        # jewllery and increment the count
        sett = {}

        for i in J:
            sett[i] = 1
        count = 0
        for i in s:
            if i in sett:
                count += 1
        return count