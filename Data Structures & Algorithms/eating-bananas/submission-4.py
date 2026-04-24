class Solution:       
    def search(self, piles, h, r, l, prev):
        print("r: " + str(r))
        print("l: " + str(l))
        mid = math.ceil((l+r)/2)
        print("mid: "+ str(mid))
        if r+1 == l:
            return l
        #Try k on piles
        used_hrs = 0
        for p in piles:
            used_hrs += math.ceil(p/mid)
        if used_hrs > h:
            return self.search(piles, h, mid, l, mid)
        else:
            return self.search(piles, h, r, mid, mid)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.search(piles, h, 0, max(piles), -1)
        #used_hrs += math.ceil(p/i)
        
            