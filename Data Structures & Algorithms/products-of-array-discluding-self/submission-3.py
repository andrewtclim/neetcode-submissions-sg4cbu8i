class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init variable to store length of array and output arr
        N = len(nums)
        res = [1] * N

        # prefix loop: res[i] will become prod of all nums to left of it
        # direction: left to right 
        prefix = 1
        for i in range(N):
            res[i] = prefix # res[i] as the prefix (prod of all elems to left)
            prefix *= nums[i] # update prefix
        
        # suffix loop: multiply res[i] by suffix (prod of everything to right)
        # direction: right to left
        suffix = 1
        for i in range(N-1, -1, -1):
            res[i] *= suffix # multiply res[i] by suffix
            suffix *= nums[i]
        
        return res
