class Solution:
    def search(self, nums: List[int], target: int) -> int:
       # initalize pointers 
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high)//2
            midpoint = nums[mid]

            if midpoint == target:
                return mid
            elif target > midpoint:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
