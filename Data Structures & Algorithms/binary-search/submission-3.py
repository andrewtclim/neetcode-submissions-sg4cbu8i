class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize low and high indicies 
        low = 0
        high = len(nums)-1

        while high >= low:
            mid = (low+high)//2
            midpoint = nums[mid]
            if midpoint == target:
                return mid
            elif midpoint < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1