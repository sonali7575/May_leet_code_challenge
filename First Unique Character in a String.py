# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictt = {}
        count = 0
        for i in s:
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1

        for i in range(len(s)):
            if dictt[s[i]] == 1:
                return i
        else:
            return -1


ob1 = Solution()
print(ob1.firstUniqChar("people"))
print(ob1.firstUniqChar("abaabba"))