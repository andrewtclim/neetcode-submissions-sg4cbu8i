class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initalize a buy and sell pointer
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # calculate profit
            profit = prices[r] - prices[l]

            if profit > 0:
                maxP = max(maxP, profit)
            else:
                l = r 
            
            r += 1
        
        return maxP