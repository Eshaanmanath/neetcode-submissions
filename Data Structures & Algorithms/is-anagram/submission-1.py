class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l=list(t)
        for i in s:
            if i in l:
                l.remove(i)
        if len(l)==0:
            return True
        return False
        