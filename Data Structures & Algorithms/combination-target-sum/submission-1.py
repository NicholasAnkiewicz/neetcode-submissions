class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Recursive call on (selected num - target) until 0
        #If reach end of list and each num < target return failure
        res = []
        def backtrack(nums, target, current):
            for i in range(len(nums)):
                if target - nums[i] == 0:
                    current.append(nums[i])
                    res.append(current[:])
                    current.pop()
                if target - nums[i] > 0:
                    current.append(nums[i])
                    backtrack(nums[i:], target-nums[i], current)
                    current.pop()
        cur = []
        backtrack(nums, target, cur)
        return res
        
        
        
        

