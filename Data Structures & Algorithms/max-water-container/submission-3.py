class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init l and r pointers 
        l, r = 0, len(heights)-1
        maxArea = 0 

        while l < r:
            length = r-l
            height = min(heights[l], heights[r])
            area = length * height 
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

