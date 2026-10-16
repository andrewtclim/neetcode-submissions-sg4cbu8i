class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # iter over possible k value rates
        l, r = 1, max(piles) 
        minSpeed = r

        while l <= r:
            k = (l+r)//2

            totalTime = sum(math.ceil(p/k) for p in piles)

            # invalid rate must speed up
            if totalTime > h:
                l = k + 1
            else:
                minSpeed = k  
                r = k - 1
        
        return minSpeed


