class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = 1
        longest = 0
        for num in nums:
            cur = dic.get(num-1,-1)
            if cur == -1 :
                cur_len = 1
                l = 0
                while l != -1:
                    l = dic.get(num+1,-1)
                    if longest < cur_len:
                        longest = cur_len
                    cur_len += 1
                    num+= 1
        return longest

                    