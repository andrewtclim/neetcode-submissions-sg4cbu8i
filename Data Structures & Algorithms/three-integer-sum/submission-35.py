class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init a res array 
        # sort the input array [-1, -1, 0, 1, 2, ...]
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # hold first value constant, skip over any duplicates 
            if i > 0 and nums[i-1] == a:
                continue
            
            # init l and r pointers for b and c 
            l, r = i+1, len(nums)-1

            # scan to find valid b and c pairs
            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a + b + c
                if curSum == 0:
                    # found triplet -> append, slide to next values
                    res.append([a, b, c])
                    l += 1
                    r -= 1
                    # skip duplicates on left side 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
            
        return res
                    
