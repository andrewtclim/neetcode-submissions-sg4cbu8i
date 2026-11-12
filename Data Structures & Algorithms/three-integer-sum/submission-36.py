class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # skip duplicate a's
            if i > 0 and a == nums[i-1]:
                continue 
            # init pointers for remainder 
            l, r = i+1, len(nums)-1

            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a + b + c
                if curSum == 0:
                    res.append([a, b, c])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1

        return res