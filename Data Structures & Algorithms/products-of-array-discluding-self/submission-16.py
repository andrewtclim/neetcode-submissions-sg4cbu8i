class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init res as 1's 
        # uses pre and post fix 

        N = len(nums)
        res = [1] * N

        # from l to r (res[i] = prod of all nums to the left of it)
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(N-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
        