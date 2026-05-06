class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        res = 0
        total = 0
        for num in nums:
            total += num
            res += dic.get(total-k, 0)
            dic[total] = dic.get(total, 0) + 1
        return res
                