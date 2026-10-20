class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        # our sol will be at nums[l] == nums[r] fully shrinked
        while l < r:
            m = (l+r)//2

            # shrink left side
            if nums[m] > nums[r]:
                l = m + 1
            # otherwise move r to the middle (nums[m] could be min so include) 
            else:
                r = m 
        
        return nums[l]


