class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # init l and r pointers (possible k values to iter over)
        l, r = 1, max(piles)
        res = r # init var to track min valid eating speed

        while l <= r:
            k = (l+r)//2 # init test speed (midpoint)

            totalTime = sum(math.ceil(p/k) for p in piles)

            if totalTime > h:
                l = k + 1 # increase your rate
            else:
                res = k # record potential rate
                r = k - 1 # decrease rate, see if we can go slower 
        
        return res