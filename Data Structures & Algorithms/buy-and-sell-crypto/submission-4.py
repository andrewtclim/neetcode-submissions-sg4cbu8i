class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initalize 2 pointers (buy and sell)
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(maxP, profit)
            # negative profit means -> found lower price (l)
            else:
                l = r
            r += 1
        
        return maxP 
