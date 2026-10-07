class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buy pointer and r = sell pointer
        # profit is prices[r]-prices[l]
        # if the profit is positive then record it, otherwise move buy pointer
        l, maxProfit = 0, 0 

        for r in range(len(prices)):
            profit = prices[r]-prices[l]
            if profit < 0:
                l = r
            maxProfit = max(maxProfit, profit)
        
        return maxProfit