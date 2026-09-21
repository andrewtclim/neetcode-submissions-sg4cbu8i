class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init a res array filled with 1's
        N = len(nums)
        res = [1] * N

        # prefix from l -> r
        # [1,2,4,6] -> [1, 1, 2, 8] (res[i] becomes prod of everything to left of it)
        pre = 1 
        for i in range(N):
            # first value res[i] from left unchanged (since init pre was 1)
            res[i] *= pre
            pre *= nums[i] 
        
        # post from r -> l
        # og array is [1,2,4,6]
        # [1,1,2,8] -> [48, 24, 12, 8]
        post = 1
        for i in range(N-1, -1, -1):
            # first value from the right remains unchanged (similar to pre)
            res[i] *= post
            # accumulate values from the r->l
            post *= nums[i]
        
        return res
