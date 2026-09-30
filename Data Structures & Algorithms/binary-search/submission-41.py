class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init a l and r pointer (start and beginning of arr)
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            mid = nums[m]
            if target == mid:
                return m
            elif target > mid:
                l = m + 1
            else:
                r = m - 1
        
        return -1