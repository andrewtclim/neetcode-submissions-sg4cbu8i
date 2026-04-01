class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initalize pointers
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        
        return maxP