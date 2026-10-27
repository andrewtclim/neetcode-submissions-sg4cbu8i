class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init a res array of 1's
        res = [1]*len(nums)

        # apply from l -> r, each entry becomes the product of everything to the left of it
        # [1,2,4,6] -> [1, 1, 2, 8]
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        
        # now apply from l <- r
        # start with [1, 1, 2, 8] and og array [1, 2, 4, 6]
        # [48 ,24 , 12, 8]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res