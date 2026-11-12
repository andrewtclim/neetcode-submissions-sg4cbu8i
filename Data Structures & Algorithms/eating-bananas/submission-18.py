class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            totalTime = sum(math.ceil(p/k) for p in piles)

            # speed up (invalid rate)
            if totalTime > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        
        return res
