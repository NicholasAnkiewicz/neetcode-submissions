class NumArray:

    def __init__(self, nums: List[int]):
        self.dic = {-1:0}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.dic[i] = total

    def sumRange(self, left: int, right: int) -> int:
        return self.dic[right] - self.dic[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)