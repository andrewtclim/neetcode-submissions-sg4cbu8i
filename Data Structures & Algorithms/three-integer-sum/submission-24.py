class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init res and sort nums 
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip all dupe a's 
            if i > 0 and a == nums[i-1]:
                continue 
            # init l and r pointers for b and c 
            l = i + 1
            r = len(nums)-1
            # twoSumII scan 
            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a + b + c
                if curSum == 0:
                    res.append([a,b,c])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
            
        return res