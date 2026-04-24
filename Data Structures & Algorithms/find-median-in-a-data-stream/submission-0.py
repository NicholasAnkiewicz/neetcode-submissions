class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()
        


    def findMedian(self) -> float:
        length = len(self.l)
        if length == 0:
            return None
        if length % 2 == 0:
            return (self.l[(int((length-1)/2))] + self.l[int((length-1)/2)+1])/2
        return self.l[int((length-1)/2)]
        
        