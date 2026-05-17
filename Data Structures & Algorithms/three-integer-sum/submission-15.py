class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init a res arr, sort nums takes O(n log n)
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip all dupe a's
            if i > 0 and a == nums[i-1]:
                continue 
            # for this a perform twoSum II, calculate b + c 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # append and skip values -> no duplicate triplets 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # ensure b is always unique as well 
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
