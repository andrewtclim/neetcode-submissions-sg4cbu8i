class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # idea: a+b+c = 0 are valid triplets (hold a constant and apply twoPointer method to 
        # values b and c)
        for i, a in enumerate(nums):
            # skip over any duplicate a's 
            if i > 0 and a == nums[i-1]:
                continue 
            # set up inital l and r pointers 
            l, r = i+1, len(nums)-1
            
            # iter through other values 
            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a+b+c
                if curSum == 0:
                    res.append([a,b,c])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1

        return res
