class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init a l, r pointer for buy and sell days
        l = 0 
        max_profit = 0 

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                # move to the next valid buying day
                l = r 
        
        return max_profit