class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = height * width 
        # height = min(l_bar, r_bar) and width = (r-l)
        l, r = 0, len(heights)-1
        maxArea = 0

        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r-l)
            maxArea = max(area, maxArea)
            
            # update bar to find larger area
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxArea

