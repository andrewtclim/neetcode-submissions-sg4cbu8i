class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init a result array 
        N = len(nums)
        res = [1] * N

        # iter from left to right with a prefix
        # [1, 2, 4, 6] -> [1, 1, 2, 8]
        prefix = 1
        for i in range(N):
            res[i] = prefix
            prefix *= nums[i]
        
        # iter from right to left
        # OG NUMS = [1, 2, 4, 6]
        # [1, 1, 2, 8] -> [48, 24, 12, 8]
        suffix = 1
        for i in range(N-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

