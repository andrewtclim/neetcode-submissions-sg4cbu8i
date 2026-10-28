class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init res array and sort nums (O (n log n))

        res = []
        nums.sort()

        # valid triplets are (a+b+c = 0)
        for i, a in enumerate(nums):
            # skip over duplicate a values
            if i > 0 and a == nums[i-1]:
                continue 
            
            # init l and r pointers (for b and c)
            l, r = i+1, len(nums)-1
            while l < r:
                b = nums[l]
                c = nums[r]
                curSum = a+b+c
                
                if curSum == 0:
                    res.append([a, b, c])
                    # update your pointers
                    l += 1
                    r -= 1
                    # skip over duplicate b values 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
