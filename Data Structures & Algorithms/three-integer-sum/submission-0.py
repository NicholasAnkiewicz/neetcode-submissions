class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for k in range(n):
            # Skip duplicate values for k
            if k > 0 and nums[k] == nums[k-1]:
                continue
                
            target = -nums[k]
            i = k + 1
            j = n - 1
            
            while i < j:
                total = nums[i] + nums[j]
                if total < target:
                    i += 1
                elif total > target:
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    # Skip duplicates for i and j
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
        return res