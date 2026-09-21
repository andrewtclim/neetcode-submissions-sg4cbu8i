class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init a var to track max profit and the buy, sell days (sliding window)
        maxProf = 0
        l, r = 0, 1

        while r < len(prices):
            # each day calc profit 
            prof = prices[r] - prices[l]
            # if the profit is positive 
            if prof > 0:
                # then record it
                maxProf = max(maxProf, prof)
            # otherwise slide your buy day to the new low
            else:
                l = r
            # go to next day
            r += 1
        
        return maxProf