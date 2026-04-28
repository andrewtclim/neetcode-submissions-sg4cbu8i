class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums and init res arr
        nums.sort()
        res = []

        # iter over all a values
        for i, a in enumerate(nums):
            # skip over all duplicate a's (ensure a is unique)
            if i > 0 and a == nums[i-1]:
                continue
            # twosum II problem 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0: 
                    res.append([a, nums[l], nums[r]])
                    # move pointers -> unique triplet always 
                    l += 1
                    r -= 1
                    # ensure b is unique as well
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else: 
                    r -= 1

        return res


