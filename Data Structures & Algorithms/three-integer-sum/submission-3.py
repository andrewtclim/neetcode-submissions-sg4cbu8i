class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init res arr and sort the input arr (O n log n)
        res = []
        nums.sort()

        # hold first number constant and loop, then loop through each a
        for i, a in enumerate(nums):
            # skip all duplicate a's
            if i > 0 and a == nums[i-1]:
                continue 
            # init the l and r (b and c indicies after a)
            l, r = i + 1, len(nums)-1
            # twosum II subproblem
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # add valid triplet and slide pointers (avoid dupes)
                    res.append([a, nums[l], nums[r]]) 
                    l += 1
                    r -= 1
                    # skip all duplicate b values 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # threeSum too large, shrink sum from the right 
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
                
