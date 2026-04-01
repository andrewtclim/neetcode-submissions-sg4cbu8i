class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init binary search pointers 
        l, r = 0, len(nums)-1 

        while l <= r:
            mid = (l + r)//2
            midp = nums[mid]
            if target == midp:
                return mid
            elif target > midp:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 