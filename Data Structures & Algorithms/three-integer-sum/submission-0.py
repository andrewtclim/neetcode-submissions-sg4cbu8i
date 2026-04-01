class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initalize solution set and sort nums
        res = []
        nums.sort()

        # [a,b,c] where a+b+c = 0 and skip duplicates 

        for i, a in enumerate(nums):
            # do not include duplicate values for a (first value, starts at i =0)
            if i > 0 and a == nums[i-1]:
                continue
            # initalize pointers
            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    # add to solution set
                    res.append([a, nums[l], nums[r]])
                    # update pointers
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res




        