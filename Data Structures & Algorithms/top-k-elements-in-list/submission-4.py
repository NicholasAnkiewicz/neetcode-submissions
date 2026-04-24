class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {1:[]}
        numc = {}
        result = []
        highest = 1
        for n in nums:
            if n in numc:
                if numc[n]+1 in freq:
                    freq[numc[n]].remove(n)
                    numc[n] += 1
                    freq[numc[n]].append(n)
                else:
                    freq[numc[n]].remove(n)
                    numc[n] += 1
                    freq[numc[n]] = [n]
                    highest = numc[n]
            else:
                numc[n] = 1
                freq[1].append(n)
        while len(result) < k:
            while len(freq[highest]) <= 0:
                highest -= 1
            result.append(freq[highest].pop())
        return result

                