class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init sliding window pointers (l=buy and r=sell)
        l, r = 0, 1
        maxP = 0 

        # iter over all the days 
        for r in range(1, len(prices)):
            prof = prices[r] - prices[l]
            if prof > 0:
                maxP = max(prof, maxP)
            else:
                # found a new day to buy stock
                l = r
        
        return maxP