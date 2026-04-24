class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while True:
            mid = (l+r)//2
            print("L: " + str(l) + " Value: " + str(nums[l]))
            print("R: " + str(r) + " Value: " + str(nums[r]))
            print("mid: " + str(mid) + " Value: "+ str(nums[mid]))
            print()
            if l+1 == r or l == r:
                if nums[l]>nums[r]:
                    return nums[r]
                else:
                    return nums[0]
            if nums[l] > nums[mid]:
                r = mid
                continue
            if nums[l] < nums[mid]:
                l = mid
