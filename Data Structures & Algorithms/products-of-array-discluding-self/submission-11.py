class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init res array and length of array 
        N = len(nums)
        res = [1] * N

        # apply prefix to the array (value is the prod of everything to left of it)
        # [1,2,4,6] -> [1,1,2,8]
        prefix = 1
        for i in range(N):
            # apply the prefix 
            res[i] = prefix 
            # update the prefix 
            prefix *= nums[i]
        
        # start from prefix-applied array (right to left)
        # [1,1,2,8] -> [48,24,12,8]
        suffix = 1
        for i in range(N-1,-1,-1):
            # apply the suffix
            res[i] *= suffix
            # update the suffix
            suffix *= nums[i]
        
        return res
