class Solution:
    def bin_s(self, nums, target, l, r):
        #print(nums[l:r+1])
        #print("l "+str(l))
        #print("r "+str(r))
        if l>=r:
            return l
        mid = (l+r)//2
        if nums[mid] == target:
            return -999
        if nums[mid] > target:
            #print(nums[r:mid])
            return self.bin_s(nums, target, l, mid)
        else:
            return self.bin_s(nums, target, mid+1, r)

    def bin_s2(self, nums, target, l, r):
        if l>=r:
            return -1
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.bin_s2(nums, target, l, mid)
        else:
            return self.bin_s2(nums, target, mid+1, r)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = []
        for i in range(len(matrix)):
            col.append(matrix[i][0]) 
        
        row = self.bin_s(col, target, 0, len(col))
        if row == -999:
            return True
        if self.bin_s2(matrix[row-1], target, 0, len(matrix[row-1])) == -1:
            return False
        return True
    
         