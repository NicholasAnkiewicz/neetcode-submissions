class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        highest = 0
        while i < j:
            if heights[i] <= heights[j]:
                if highest < heights[i] * (j-i):
                    highest = heights[i] * (j-i)
                i += 1
            else:
                if highest < heights[j] * (j-i):
                    highest = heights[j] * (j-i)
                j -= 1
        return highest
