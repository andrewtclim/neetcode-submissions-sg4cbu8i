class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        # nums[r] will always be the 
        # finish running when nums[l]==nums[r] which the min 
        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1 # elim left side 
            else:
                r = m # move right pointer to mid 
        
        return nums[l]