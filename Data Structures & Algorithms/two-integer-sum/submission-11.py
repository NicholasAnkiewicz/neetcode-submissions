class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for n in range(len(nums)):
            i = c.get(nums[n], -1)
            if i != -1:
                return [i, n] 
            c[target-nums[n]] = n
                
            