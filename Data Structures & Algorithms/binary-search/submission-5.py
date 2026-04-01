class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize left and right pointers
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            midpoint = nums[mid]
            if midpoint == target:
                return mid 
            elif midpoint < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # not found in nums
        return -1
