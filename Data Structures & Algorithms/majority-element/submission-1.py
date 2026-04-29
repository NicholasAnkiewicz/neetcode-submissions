class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = -1
        cur_freq = 0
        for num in nums:
            if res == num:
                cur_freq += 1
            else:
                cur_freq -= 1
            if cur_freq <= 0:
                res = num
                cur_freq = 1
        return res
