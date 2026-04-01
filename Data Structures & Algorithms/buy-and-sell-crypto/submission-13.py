class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init two pointers (sliding window)
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # calculate profit 
            prof = prices[r] - prices[l]
            if prof > 0:
                maxP = max(prof, maxP)
            else:
                l = r
            # move up a day 
            r += 1
        
        return maxP
