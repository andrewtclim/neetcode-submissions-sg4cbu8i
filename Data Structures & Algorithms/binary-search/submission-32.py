class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init l and r pointers 
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            mid = nums[m]
            if target == mid:
                return m 
            # eliminate bottom half
            elif target > mid:
                l = m + 1
            else:
                r = m - 1
        
        return -1