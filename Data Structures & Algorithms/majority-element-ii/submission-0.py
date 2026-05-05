class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)//3
        res = set()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > n:
                res.add(num)
        return [*res]