class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            k = (l+r)//2
            totalTime = sum(math.ceil(p/k) for p in piles)

            # invalid rate, must speed up
            if totalTime > h:
                l = k + 1
            # valid rate, record and try to search for another
            else:
                res = k 
                r = k - 1
        
        return res

