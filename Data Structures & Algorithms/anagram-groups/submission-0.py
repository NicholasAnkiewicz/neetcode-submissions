class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        curM = {}
        for i in range(len(strs)):
            sort1 = str(sorted(strs[i]))
            cur = curM.get(sort1, -1)
            if cur != -1:
                curM[sort1].append(strs[i])
            else:
                curM[sort1] = [strs[i]]
        return curM.values()