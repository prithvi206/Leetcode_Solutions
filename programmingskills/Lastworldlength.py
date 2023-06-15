# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)-1
        s = s.split(' ')
        return len(s[n])
