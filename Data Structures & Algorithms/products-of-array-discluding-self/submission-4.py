class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init a res array and var for len(nums)
        N = len(nums)
        res = [1] * N

        # suffix : res[i] = prod of all nums left of res[i]
        suffix = 1
        for i in range(N):
            res[i] = suffix
            suffix *= nums[i]
        
        # postfix : res[i] = prod of all nums to the right of res[i]
        postfix = 1
        for i in range(N-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
