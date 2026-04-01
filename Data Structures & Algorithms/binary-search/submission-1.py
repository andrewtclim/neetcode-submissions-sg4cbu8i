class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize pointers for the first and last index
        low, high = 0, len(nums)-1

        # iterate until this is only one num*
        while high >= low:
            mid = (low + high)//2
            midpoint = nums[mid]
            if midpoint == target:
                return mid
            elif target > midpoint:
                low = mid + 1
            else:
                high = mid - 1
        
        # does not exists in nums
        return -1