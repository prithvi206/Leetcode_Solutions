"""345 Reverse Vowels of a String"""




class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        v = 'aeiouAEIOU'
        l,r = 0,len(s)-1
        while l<r:
            if s[l] not in v and s[r] not in v:
                l+=1
                r-=1
            if s[l] not in v :
                l+=1
            elif s[r] not in v:
                r-=1
            else:
                s[l] ,s[r] = s[r],s[l]
                l+=1
                r-=1
        return ''.join(s)
