class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initalize two pointers (buy and sell days)
        # variable to store max profit
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            profit = prices[r]-prices[l]
            # no profit made
            if profit < 0:
                # found a new buying day (low price)
                l = r
            # positive profit found
            else:
                maxP = max(maxP, profit)
            # always increment by one day 
            r += 1
        
        return maxP
