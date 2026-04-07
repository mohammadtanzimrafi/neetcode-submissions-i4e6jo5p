class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True

        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        for check in range(len(s)):
            if len(sorted_s) != len(sorted_t):
                flag = False
                break
            if sorted_s[check] != sorted_t[check]:
                flag = False

        return flag