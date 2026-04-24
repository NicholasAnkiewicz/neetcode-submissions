class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        curM = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            freq = tuple(counts)
            if freq not in curM:
                curM[freq] = []
            curM[freq].append(s)
        return list(curM.values())

            