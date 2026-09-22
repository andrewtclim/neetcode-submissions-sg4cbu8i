class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first which takes O(nlogn), our solution will have a nested for loop thus O(n^2)
        nums.sort()
        res = []

        # hold a constant then search over valid b and c values, then move to next a value
        for i, a in enumerate(nums):
            # skip over any duplicate a's but always process the first a-value
            if i > 0 and a == nums[i-1]:
                continue 
            # otherwise scan for valid triplets
            l = i + 1
            r = len(nums)-1

            # apply twoSum II algo 
            while l < r:
                curSum = a + nums[l] + nums[r]
                if curSum == 0:
                    # found triplet -> append and skip over any dupes
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip any duplicate b values
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # curSum is too small and we want to increase
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
