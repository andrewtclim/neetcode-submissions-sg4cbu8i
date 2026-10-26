class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # iter over all possible k-values 
        l, r = 1, max(piles)
        res = r # init a min possible speed 

        while l <= r:
            k = (l+r)//2

            totalTime = sum(math.ceil(p/k) for p in piles)

            # speed up 
            if totalTime > h:
                l = k + 1
            else:
                res = k # update your res variable
                r = k - 1
        
        return res
