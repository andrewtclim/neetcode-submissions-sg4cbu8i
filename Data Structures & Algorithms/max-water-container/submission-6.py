class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init maxArea variable and two pointers
        maxArea = 0 
        l, r = 0, len(heights)-1

        while l < r:
            # calculate the current area = length * height
            area = (r-l) * (min(heights[l], heights[r]))
            maxArea = max(area, maxArea)
            # update to get a better height if possible 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea