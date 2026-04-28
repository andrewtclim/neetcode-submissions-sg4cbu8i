class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort input arr and init res
        nums.sort()
        res = []

        # iter over all a's
        for i, a in enumerate(nums):
            # skip duplicate a's
            if i > 0 and a == nums[i-1]:
                continue 
            # init l and r pointers for b and c 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # add valid triplet and slide to avoid duplicates
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # avoid duplicate b's 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res