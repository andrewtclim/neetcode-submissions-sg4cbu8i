class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy
            if profit > 0:
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
