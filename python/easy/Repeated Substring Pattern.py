class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)

        for n in range(1, l // 2 + 1):
            if l % n == 0 and s[:n] * (l // n) == s:
                return True

        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        t = s + s

        if s in t[1: -1]:
            return True
        return False
