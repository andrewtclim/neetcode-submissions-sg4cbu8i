class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init len of nums and also a result array 
        N = len(nums)
        res = [1] * N 

        # l to r pass: ensure that res[i] = prod of all nums to the left of it 
        pre = 1
        for i in range(N):
            # update res[i]
            res[i] *= pre
            # update prefix
            pre *= nums[i]
        
        # r to l pass: ensure that res[i] is the prod of all nums to the right of it
        suf = 1
        for i in range(N-1, -1, -1):
            # update res[i]
            res[i] *= suf
            # update suffix
            suf *= nums[i]
        
        return res