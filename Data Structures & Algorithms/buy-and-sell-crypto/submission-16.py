class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init sliding window pointers (l=buy and r=sell)
        l, r = 0, 1
        maxP = 0 

        # iter over all the days 
        # NOTE: Here I let the right pointer be in the range of indices of prices
        # So I didnt really need to init r above, but either works (manually updating r)
        for r in range(1, len(prices)):
            prof = prices[r] - prices[l]
            if prof > 0:
                maxP = max(prof, maxP)
            else:
                # found a new day to buy stock
                l = r
        
        return maxP