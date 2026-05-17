class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointer Linear Solution in O(n)
        # init l and r pointers at each end 
        l, r = 0, len(heights)-1
        res = 0

        while l < r:
            left_bar, right_bar = heights[l], heights[r]
            # calc area = width * height
            area = (r-l) * min(left_bar, right_bar)
            # update result 
            res = max(res, area)
            # try to get a higher height in the next iter
            if right_bar > left_bar:
                l += 1
            else:
                r -= 1
        
        return res
