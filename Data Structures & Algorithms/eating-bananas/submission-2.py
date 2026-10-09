class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Modified Binary Search: that searches through k-values (1 to max(piles))

        Valid rates (k): when koko eats bananas within the h hour
        if invalid (totalTime > h) -> increase eating rate l = k + 1
        if valid (totalTime <= h) -> see if there are slower valid eating rates: r = k + 1 
        '''
        l, r = 1, max(piles)
        minSpeed = r # init minSpeed (at first) to be r (because we know this must be a valid speed)

        while l <= r:
            # mid point
            k = (l+r)//2

            # calc total time: bananas/rate rounded up -> time it takes Koko to finish pile p
            totalTime = sum(math.ceil(p/k) for p in piles)

            # koko would get caught
            if totalTime > h:
                # increase eating rate
                l = k + 1
            else:
                # record the valid rate
                minSpeed = k
                # update right pointer to check slower speeds
                r = k - 1
                
        return minSpeed
        


            