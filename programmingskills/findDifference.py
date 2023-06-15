# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S=list(s)
        S.sort()
        T=list(t)
        T.sort()
        for i in range(len(S)):
            if T[i]!=S[i]:
                return T[i]
        return T[-1]