class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        l = True
        if len(s) != len(t):
            return False
        for c in s:
            if c in t:
                t = t.replace(c, "", 1)
            else:
                l = False
        return l