class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 

        while l <= r:
            mid = (l+r)//2
            midpoint = nums[mid]
            if midpoint == target:
                return mid
            # eliminate bottom half (by raising the floor)
            elif target > midpoint:
                l = mid + 1
            # eliminate top half (by lowering the ceiling)
            else:
                r = mid -1
        
        return -1

        