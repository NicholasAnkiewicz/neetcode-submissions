class Solution:       
    def search(self, piles, h, l, r, prev):
        mid = math.ceil((l+r)/2)
        print("r: " + str(r))
        print("l: " + str(l))
        print("mid: "+ str(mid))
        if r == l+1 or r == l:
            return r
        #Try k on piles
        used_hrs = 0
        for p in piles:
            used_hrs += math.ceil(p/mid)
        if used_hrs > h:
            return self.search(piles, h, mid, r, mid)
        else:
            return self.search(piles, h, l, mid, mid)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.search(piles, h, 0, max(piles), -1)
        #used_hrs += math.ceil(p/i)
        
            