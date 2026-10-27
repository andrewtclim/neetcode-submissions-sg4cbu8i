class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # result rate variable (min valid speed)

        while l <= r:
            k = (l+r)//2 # check middle rate 
            totalHours = sum(math.ceil(p/k) for p in piles)

            if totalHours > h:
                # elim bottom rates
                l = k + 1
            else:
                res = k # record new min valid rate 
                r = k - 1 # check other rates 
        
        return res