class Solution:
    def bin_s(self, nums, target, r, l):
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if l-r < 2:
            return -1
        if nums[mid] > target:
            print(nums[r:mid])
            return self.bin_s(nums, target, r, mid)
        else:
            print(nums[mid:l])
            return self.bin_s(nums, target, mid, l)
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_s(nums, target, 0, len(nums))
         
         