class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init l and r pointers 
        l, r = 0, len(nums)-1

        while l <= r:
            # find midpoint index 
            m = (l+r)//2
            mid = nums[m]
            # found target -> return it's index 
            if target == mid:
                return m
            # eliminate bottom half, target is larger than midpoint            
            elif target > mid:
                l = m + 1
            else:
                r = m - 1
        
        return -1
