class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {i: [] for i in range(1, len(nums)+1)}
        numc = {}
        result = []
        for n in nums:
            numc[n] = numc.get(n, 0)+1
        for num, fre in numc.items():
            freq[fre].append(num)

        for i in range(len(freq), 0, -1):
            while len(freq[i]) > 0:
                result.append(freq[i].pop())
                if len(result) == k:
                    return result

                