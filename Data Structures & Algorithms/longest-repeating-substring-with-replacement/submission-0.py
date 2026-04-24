class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dic = {}
        cur_maxf = 0
        res = 0
        left_p = 0
        for i in range(0, len(s)):
            if s[i] in freq_dic:
                freq_dic[s[i]] += 1
            else:
                freq_dic[s[i]] = 1
            cur_maxf = max(freq_dic[s[i]], cur_maxf)
            while (((i - left_p) - cur_maxf)+1) > k:
                freq_dic[s[left_p]] -= 1
                left_p += 1
            res = max(res, i-left_p+1)
        return res
        

        