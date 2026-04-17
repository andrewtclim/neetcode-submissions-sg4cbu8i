class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TIME: O(n log n) + O(n^2) -> O(n^2)
        # init a res arr and sort input array 
        # valid threeSum: a + b + c = 0
        res = []
        nums.sort()

        # hold first num constant as a 
        for i, a in enumerate(nums):
            # skip duplicate a's 
            if i > 0 and a == nums[i - 1]:
                continue
            # init two pointers for essentially twosum II
            l = i + 1
            r = len(nums)-1
            while l < r:
                b = nums[l]
                c = nums[r]
                threeSum = a + b + c
                if threeSum == 0:
                    res.append([a, b, c])
                    l += 1
                    # skip duplicate l's (duplicate b's)
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res


