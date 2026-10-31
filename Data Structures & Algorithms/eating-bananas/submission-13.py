class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # init two pointers l and r 
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            k = (l+r)//2

            totalTime = sum(math.ceil(p/k) for p in piles)

            # invalid time -> raise rate 
            if totalTime > h:
                l = k + 1
            else:
                # update res variable, attempt lower rates
                res = k 
                r = k - 1
        
        return res
