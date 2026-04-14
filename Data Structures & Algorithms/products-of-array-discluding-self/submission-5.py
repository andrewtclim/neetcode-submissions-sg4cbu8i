class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init resulting arr
        N = len(nums)
        res = [1] * N

        # prefix -> res[i] = prod of all nums to the left of i
        prefix = 1
        for i in range(N):
            res[i] = prefix 
            prefix *= nums[i]
        
        # suffix -> res[i] = prod of all nums to right of i 
        # start from right to left
        suffix = 1
        for i in range(N-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
