class Solution:
    def bin_s(self, nums, target, r, l):
        if r>=l:
            return -1
        mid = (l+r)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            print(nums[r:mid])
            return self.bin_s(nums, target, r, mid)
        else:
            print(nums[mid:l])
            return self.bin_s(nums, target, mid+1, l)
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_s(nums, target, 0, len(nums))
         
         