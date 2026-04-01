class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize pointers from both sides
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            midpoint = nums[mid]
            if target == midpoint:
                return mid
            elif target > midpoint:
                # eliminate bottom half 
                l = mid + 1
            else:
                # eliminate top half 
                r = mid - 1
        
        # not found
        return -1