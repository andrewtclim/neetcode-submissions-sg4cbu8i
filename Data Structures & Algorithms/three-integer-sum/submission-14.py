class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort nums, init arr
        nums.sort()
        res = []

        # hold a constant, iterate over others 
        # then move onto next a 
        for i, a in enumerate(nums):
            # skip duplicate a's
            if i > 0 and nums[i-1] == a:
                continue
            # twosumII
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # additional ensure b is always unique as well 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else: 
                    r -= 1
        
        return res
