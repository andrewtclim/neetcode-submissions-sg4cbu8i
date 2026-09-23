class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # hold a constant and scan for b and c values
        # find triplets [a,b,c] 
        for i, a in enumerate(nums):
            # skip any duplicate a's 
            if i > 0 and a == nums[i-1]:
                # skip to next a value
                continue
            # init l and r pointers
            l = i + 1
            r = len(nums)-1
            # use two pointers to scan for valid b and c's 
            while l < r:
                b, c = nums[l], nums[r]
                curSum = a+b+c
                if curSum == 0:
                    res.append([a,b,c])
                    # avoid duplicates
                    l += 1
                    r -= 1
                    # ensure unique b values
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # increase curSum 
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res