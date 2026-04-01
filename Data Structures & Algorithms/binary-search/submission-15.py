class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize two pointers 
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            midpoint = nums[mid]
            if target == midpoint:
                return mid
            elif target > midpoint:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1