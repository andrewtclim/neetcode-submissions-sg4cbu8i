class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N

        prefix = 1
        # prod of everything to the left of it
        # nums = [1,2,4,6] -> res = [1, 1, 2, 8]
        for i in range(N):
            # set res to the prefix value
            res[i] = prefix
            # update the prefix value (accumulate from the last prod)
            prefix *= nums[i]

        suffix = 1
        # prod of everything to the right of it 
        # original nums = [1,2,4,6] -> start res = [1, 1, 2, 8]
        # final res = [48, 24, 12, 8] so iter: (2 * 6) then (1 * 24) then (1 * 48)
        for i in range(N-1, -1, -1):
            # multiply our suffix 
            res[i] *= suffix
            # update our suffix
            suffix *= nums[i]
        
        return res
