class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init a max area var and two pointers 
        maxArea = 0
        l, r = 0, len(heights)-1

        while l < r:
            # area = length * height
            area = (r-l) * min(heights[l], heights[r])
            # record max area
            maxArea = max(area, maxArea)
            # update bars (tiebreakers dont matter -> either bar becomes the bottleneck)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea 