class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initalize two pointers (one for a buy day and a sell day) 
        # and a var to track max profit
        # r will be current day (init in loop)
        l = 0 
        maxProf = 0 

        for r in range(1, len(prices)):
            # eval the profit at this current day (and your current buy price)
            prof = prices[r] - prices[l]
            # if the profit is positive -> update our maxProfit
            if prof > 0:
                maxProf = max(maxProf, prof)
            # if the profit is negative or even, slide your buy date to this potential new low price 
            else:
                l = r
        
        return maxProf


