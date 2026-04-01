class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init two pointers for sliding window (l=buy and r=sell)
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            prof = prices[r] - prices[l]
            if prof > 0:
                maxP = max(maxP, prof)
            else:
                l = r
            r += 1
        
        return maxP
