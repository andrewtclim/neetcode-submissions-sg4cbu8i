class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize pointers for binary search 
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            midpoint = nums[m]
            # eliminate top half (small nums)
            if target > midpoint:
                l = m + 1
            # eliminate bot half (large nums)
            elif target < midpoint:
                r = m - 1
            # found target, it will be at m-pointer or m-index
            elif target == midpoint:
                return m 
        
        # loop ends target not found -> target not in nums
        return -1
