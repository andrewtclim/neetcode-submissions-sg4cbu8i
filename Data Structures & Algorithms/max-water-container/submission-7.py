class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # NOTE: Area = Length * Height
        # init l and right pointers 
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            # define area 
            area = (r-l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea) 
            # update to find the best height at each iteration 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea