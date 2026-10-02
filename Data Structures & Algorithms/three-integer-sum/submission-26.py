class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init result array and also sorts the input array 
        nums.sort()
        res = []

        # idea: a + b + c = 0 is a valid triplet
        # hold a constant and loop over b and c pairs, continue to exhaust

        for i, a in enumerate(nums):
            # skip over duplicate a's (always process first one)
            if i > 0 and a == nums[i-1]:
                continue 
            # init l and r 
            l = i + 1
            r = len(nums)-1

            while l < r:
                b, c = nums[l], nums[r]
                curSum = a + b + c
                if curSum == 0:
                    res.append([a,b,c])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1

        return res

            
