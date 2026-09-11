class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init l and r indicies 
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            mid = nums[m]

            # found target 
            if target == mid:
                return m
            # elim left half 
            elif target > mid:
                l = m + 1
            # elim right half
            else:
                r = m - 1
        
        return -1
