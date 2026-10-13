class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # iterate over a values, then look for valid b and c pairs s.t. a+b+c = 0
        for i, a in enumerate(nums):
            # skip over anyy duplicate a values (always process first one)
            if i > 0 and a == nums[i-1]:
                continue 
            # init pointers for b and c values
            l, r = i+1, len(nums)-1

            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a + b + c
                if curSum == 0:
                    res.append([a, b, c])
                    # slide pointers
                    l += 1
                    r -= 1
                    # ensure b is unique 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # too large, decrement from right
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res

