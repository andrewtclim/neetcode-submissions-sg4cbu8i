class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init res arr and sort nums (O n log n)
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue 
            l, r = i+1, len(nums)-1

            # loop to find 
            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a + b + c
                if curSum == 0:
                    res.append([a, b, c])
                    # skip to next b and c values
                    l += 1
                    r -= 1
                    # skip duplicate values of b 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
                        
