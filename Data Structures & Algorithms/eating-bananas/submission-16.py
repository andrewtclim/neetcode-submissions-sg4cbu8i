class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # midpoint
            k = (l+r)//2

            # calc total time koko takes
            totalTime = sum(math.ceil(p/k) for p in piles)

            if totalTime > h:
                l = k + 1
            else:
                res = k 
                r = k - 1
            
        return res
