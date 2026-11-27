class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        else:
            return False

# Approach 1: Sorted the arrays and compared them.

    def isAnagram2(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if  len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

# Approach: Instead of comparing entire string, compare character  by character
# and once a character mismatch happens (post sorting), return False.