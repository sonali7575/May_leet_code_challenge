#  Given an arbitrary ransom note string and another string containing letters
#  from all the magazines, write a function that will return true if the ransom note can be constructed
#  from the magazines ; otherwise, it will return false. Each letter in the magazine string can only be used once in your ransom note.
# eg : canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# ----------------------------------------------------------------------------
# method 1 using Counters

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return (Counter(ransomNote) - Counter(magazine)) == {}

#     -------------------------------------------------------------------------
#   method 2 using the defaultdict

from collections import defaultdict

def canConstruct( ransomNote: str, magazine: str) -> bool:
    # creates an empty dict of type int
    dictt = defaultdict(int)
    for letters in magazine:
#         print(dictt[letters])
        dictt[letters] = dictt[letters] +1
    for letters in ransomNote:
#         print(dictt[letters])
        if dictt[letters] == 0:
            return False
        dictt[letters] = dictt[letters]-1
    return True