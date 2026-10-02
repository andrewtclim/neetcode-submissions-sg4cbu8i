class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init result array and sort nums (O(nlogn))
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # always process first one and skip duplicates after
            if i > 0 and a == nums[i-1]:
                continue 
            # init l and r pointers 
            l, r = i + 1, len(nums)-1

            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a + b + c
                if curSum == 0:
                    res.append([a, b, c])
                    l += 1
                    # skip duplicate b's 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
            
        return res
