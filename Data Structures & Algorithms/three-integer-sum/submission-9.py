class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums 
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # skip all duplicate a's
            if i > 0 and a == nums[i-1]:
                continue 
            # find valid b and c's with our a held constant 
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # attach valid pair -> slide pointers to ensure unique triplets
                    res.append([a, nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    # ensure b is always unique 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # decrease our threeSum value
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
