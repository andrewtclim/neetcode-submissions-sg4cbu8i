class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            # middle value is the current checking rate 
            k = (l+r)//2

            # see if rate is valid
            totalTime = sum(math.ceil(p/k) for p in piles)

            # invalid case -> speed up rate (elim left half)
            if totalTime > h:
                l = k + 1
            # valid case: record and see if there are any slower rates available
            else:
                res = k
                r = k - 1

        return res