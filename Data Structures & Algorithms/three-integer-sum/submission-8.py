class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort input array and init res arr
        nums.sort()
        res = []

        # hold a constant, search for valid b and c pairs
        for i, a in enumerate(nums):
            # contiguous arr -> skip any duplicate a's 
            if i > 0 and a == nums[i-1]:
                continue 
            # search for valid b and c
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # append the valid triplet 
                    res.append([a, nums[l], nums[r]])
                    # move pointers to ensure uniqueness
                    l += 1
                    r -= 1
                    # also ensure b is unique 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # value too big (decrease)
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res