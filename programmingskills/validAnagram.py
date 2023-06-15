# 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, r1 = Counter(s),Counter(t)
        if s1 & r1==s1 and s1& r1 ==r1:
            return True
        return False