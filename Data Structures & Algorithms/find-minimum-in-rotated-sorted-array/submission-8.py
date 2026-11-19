class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init pointers
        l, r = 0, len(nums)-1

        # algo stops when nums[l] == nums[r]
        # NOTE: nums[r] is either the min or the lower bound 
        while l < r:
            m = (l+r)//2
            mid = nums[m]

            if mid > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
