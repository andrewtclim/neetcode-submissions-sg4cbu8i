class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Use sliding window to determine largest area 
        Area defined as length * height 
        Height will be defined as the minimum value btwn l_bar and r_bar
        Length will be defined as r - l 
        '''
        maxArea = 0 
        l, r = 0, len(heights)-1

        while l < r:
            l_bar, r_bar = heights[l], heights[r]
            height = min(l_bar, r_bar)
            length = r - l 
            area = height * length 
            maxArea = max(maxArea, area)
            if l_bar < r_bar:
                l += 1
            else:
                r -= 1
        
        return maxArea
