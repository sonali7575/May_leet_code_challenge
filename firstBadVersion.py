# 00001111
first_bad = 0


def isBadVersion(version):
    if version >= first_bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        if n < 2:
            return n
        lb = 1
        ub = n
        while (lb <= ub):
            midpos = (lb + ub) // 2
            if isBadVersion(midpos) is not isBadVersion(midpos - 1):
                return midpos

            elif isBadVersion(midpos - 1):
                ub = midpos - 1

            else:
                lb = midpos + 1


sol = Solution()
first_bad = 4
res = sol.firstBadVersion(4)
print(res)



