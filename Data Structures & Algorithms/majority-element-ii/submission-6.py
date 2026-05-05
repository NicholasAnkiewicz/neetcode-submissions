class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candid1 = -1
        candid2 = -1
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if candid1 == num:
                cnt1 += 1
            elif candid2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                candid1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candid2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            #print(str(candid1) + ": " + str(cnt1) + "   " + str(candid2) + ": " + str(cnt2))
        
        count1, count2 = 0,0
        for i in nums:
            if i == candid1:
                count1 += 1
            if i == candid2:
                count2 += 1
        res = []
        if count1 > len(nums)//3:
            res.append(candid1)
        if count2 > len(nums)//3:
            res.append(candid2)
        return res
            
            