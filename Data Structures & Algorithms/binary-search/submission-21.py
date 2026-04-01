class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize two pointers l and r 
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            midpoint = nums[m]
            if target == midpoint:
                return m
            elif target > midpoint:
                l = m + 1
            else:
                r = m - 1
        
        return -1