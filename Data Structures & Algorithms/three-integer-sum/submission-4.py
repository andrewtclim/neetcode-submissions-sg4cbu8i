class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort arr and init res array 
        res = []
        nums.sort()
        
        # iterate over all a's 
        for i, a in enumerate(nums):
            # skip over any duplicate a's 
            if i > 0 and a == nums[i-1]: 
                continue 

            # Find the corresponding b and c values 
            l = i + 1
            r = len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                # found valid triplet : add, move pointers to avoid dupes
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # make sure l is unique 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
    
        return res
        
        

