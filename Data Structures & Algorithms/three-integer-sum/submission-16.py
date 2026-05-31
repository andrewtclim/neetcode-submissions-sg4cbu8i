class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init res and sort nums 
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # when [a+b+c] = 0 then valid triplet
            # idea: hold a constant and find valid b and c values to add to res  
            # skip any duplicate a's 
            if i > 0 and a == nums[i-1]:
                continue
            # valid a to check... 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # found valid triplet, append then slide to avoid duplicates
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # ensure l is always unique as well 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res