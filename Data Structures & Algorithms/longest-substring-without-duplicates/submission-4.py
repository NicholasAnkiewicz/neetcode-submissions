class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s == "":
            return 0
        if s == " ":
            return 1
        sub = set()
        j = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in sub:
                if len(sub) > longest:
                    longest = len(sub)
                while s[i] in sub:
                    sub.remove(s[j])
                    j += 1
                
            sub.add(s[i])
        if len(sub) > longest:
            longest = len(sub)
        if j == 0:
            return len(s)
        else:
            return longest
