class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort the nums -> O(n log n)
        nums.sort()
        res = []

        # def triplet [a, b, c] where a + b + c = 0
        for i, a in enumerate(nums):
            # skip all duplicate a's
            if i > 0 and nums[i-1] == a:
                # continue to look at the b and c
                continue 
            # set up twoSum II 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # ensure l is unique (b is unique)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res