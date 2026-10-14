class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Search through possible k-values from 1 to the max(piles)
        If the totalTime it takes koko to eat is greater than h: 
            increase your rate by l = k + 1 (elim slower rates)
        otherwise record valid rate and see if you can get a slower valid rate
            by r = k - 1
        '''
        l, r = 1, max(piles)
        minRate = r

        while l <= r:
            # check middle rate
            k = (l+r)//2

            # calc the totalTime using the k-th eating rate 
            totalTime = sum(math.ceil(p/k) for p in piles)

            # hurry up!
            if totalTime > h:
                l = k + 1
            else:
                minRate = k 
                r = k - 1
        
        return minRate
