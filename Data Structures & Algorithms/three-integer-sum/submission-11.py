class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init a res array and sort numbers 
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # ensure that a is unique 
            if i > 0 and nums[i-1] == a:
                # go to next a
                continue 
            
            # init l and r for twosum II 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # ensure l is unique (skip all repeats from left side)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
