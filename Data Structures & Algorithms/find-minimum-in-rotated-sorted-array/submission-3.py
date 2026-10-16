class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init bin search pointers 
        # logic: nums[r] is always a member of the right half (or it IS the min itself)
        # at the very end when you find the 
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2

            # if our midpoint is larger than right value
            # we can eliminate the left part of the array
            if nums[m] > nums[r]: 
                l = m + 1
            # otherwise we move the right pointer to the middle
            else:
                r = m
            
        return nums[r]