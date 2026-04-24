class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = {}
        for n in nums:
            ns[n] = 1 + ns.get(n, 0)
        for l in range(len(nums)):
            if ns[nums[l]] > 1:
                ns[nums[l]] = ns[nums[l]] -1    
            else:  
                del ns[nums[l]]
            s = ns.get(target-nums[l], -1)
            if s != -1:
                return [l, nums.index(target-nums[l],l+1)]
                 
            