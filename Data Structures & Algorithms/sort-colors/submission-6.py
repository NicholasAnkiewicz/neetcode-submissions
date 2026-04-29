class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        high = len(nums)-1
        low = 0
        cur = 0
        while cur <= high:
            if nums[cur] == 0:
                nums[cur] = nums[low]
                nums[low] = 0
                low += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur] = nums[high]
                nums[high] = 2
                high -= 1

        