class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        lowest_d = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < lowest_d:
                lowest_d = prices[i]
                continue
            else:
                if prices[i] - lowest_d > profit:
                    profit = prices[i]-lowest_d
        return profit
