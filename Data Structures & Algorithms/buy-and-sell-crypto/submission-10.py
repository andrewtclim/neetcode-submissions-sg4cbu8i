class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initalize pointers in sliding window 
        l, r = 0, 1
        # initalize max profit variable 
        maxP = 0 

        while r < len(prices):
            # profit = sell-buy
            profit = prices[r]-prices[l]
            # update maxP for every positive profit seen
            if profit > 0:
                maxP = max(profit, maxP)
            # negative or no profit -> slide buying window to right
            else:
                l = r 
            # update day
            r += 1
        
        return maxP