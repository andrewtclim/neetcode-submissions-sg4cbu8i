class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init l and r pointers
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            profit = prices[r]-prices[l]
            if profit > 0:
                maxP = max(profit, maxP)
            else:
                # found new low price
                l = r
            # update day 
            r += 1
        
        return maxP