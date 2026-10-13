class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        LOGIC: Want the minimum valid eating speed
        iterate over all the k rates from 1 to max(piles)
        totalTime = sum over bananas_each_pile/eating_rate
        if the totalTime is invalid (> h) then we raise eating speed by
        l = k + 1
        otherwise if it is valid, record rate k, then slide r = k-1 to 
        see if we can get anoter valid speed that is slower
        '''
        l, r = 1, max(piles)
        minSpeed = r

        while l <= r:
            # midpoint 
            k = (l+r)//2

            # calc time required
            totalTime = sum(math.ceil(p/k) for p in piles)

            # too slow need to increase rate
            if totalTime > h:
                l = k + 1
            else:
                # record valid speed
                minSpeed = k
                r = k - 1
        
        return minSpeed