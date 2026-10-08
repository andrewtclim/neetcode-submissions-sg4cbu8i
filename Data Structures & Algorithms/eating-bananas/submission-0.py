class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Modified Binary Search Algorithim 
        Perform Binary search from 1 to the max amount of bananas in one pile 

        Valid (in context of problem)
        - k (rates) where koko can eat all the bananas with h (hour)

        Logic:
        - if the current k is valid: record, then check if there is a slower rate that exists (move r)
        - if current k is invalid: must increase the eating rate (move l up) 
        '''
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # current k-value to check (midpoint)
            k = (l+r)//2

            # calc number of hours it takes koko to eat
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)

            # valid rate (record and see if there is a smaller k)
            if totalTime <= h:
                res = k
                r = k - 1
            # invalid rate (must increase rate)
            else:
                l = k + 1

        return res
