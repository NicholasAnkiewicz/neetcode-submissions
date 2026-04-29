class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first_string = strs[0]
        for i in range(len(first_string)):
            for j in range(1, len(strs)):
                other_string = strs[j]
                if i+1 > len(other_string) or first_string[i] != other_string[i]:
                    return res
            res += strs[0][i]
        return res


