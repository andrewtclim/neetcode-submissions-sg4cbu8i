class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iter through array with two pointers for buy and sell 
        l, r = 0, 1
        final_profit = 0

        # iter through days
        while r < len(prices):
            # calc profit 
            profit = prices[r] - prices[l]
            # when profit is pos -> add to final profit 
            if profit > 0:
                final_profit += profit
            # update days 
            l += 1
            r += 1
        
        return final_profit
            