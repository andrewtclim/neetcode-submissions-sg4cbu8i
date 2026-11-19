class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2
            mid = nums[m]

            if mid > nums[r]:
                # everything left of m is bigger than nums[r] (b.c. its ascending)
                # therefore elim the left half
                l = m + 1
            else:
                # move r to the middle point (it COULD be the min or is the new lower anchor)
                r = m
        
        # when l and r intersect we have found our minimum
        return nums[l]
