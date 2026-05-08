class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        booleans = [False]*len(nums)
        for num in nums:
            if num > 0 and num <= len(nums):
                booleans[num-1] = True
        for i in range(len(booleans)):
            if booleans[i] == False:
                return i+1
        return len(nums) + 1
            
        
            
