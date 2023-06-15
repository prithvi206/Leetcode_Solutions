# 744. Find Smallest Letter Greater Than Target


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = -1
        e = len(letters)-1
        while s+1<e:
            mid = (s+e)//2
            if letters[mid]>target:
                e = mid
            else:
                s = mid
        return letters[e] if letters[e]>target else letters[0]