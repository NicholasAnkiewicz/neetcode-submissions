class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1   
        if nums[-1] >= nums[0]:
            while l <= r:  
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid - 1  
                else:
                    l = mid + 1
            return -1
        
        #Find pivot
        while l+1 != r:
            mid = (l+r)//2
            print("L: " + str(l))
            print("R: " + str(r))
            print("mid: " + str(mid))
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        
        #Select target sub array 
        if target > nums[-1]:
            r = l
            l = 0
        else:
            l = r
            r = len(nums)-1
        #Perform binary search on subarray
        while l <= r:  
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1  
            else:
                l = mid + 1
        return -1
        
