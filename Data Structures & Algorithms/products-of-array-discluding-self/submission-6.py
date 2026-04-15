class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init res arr
        res = [1] * len(nums)

        # update res[i] = prod of all nums to left of i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # update res[i] so it equals the product of all left numbers (not itself)
            prefix *= nums[i] # accums from left -> right
        
        # update res[i] = prod of all nums to right of i (as well, accumulate products)
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i] # accum from left <- right

        return res 
