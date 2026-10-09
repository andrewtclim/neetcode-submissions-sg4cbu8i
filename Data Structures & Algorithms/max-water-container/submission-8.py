class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Use two pointers that start at each end. The height of box is min(l_bar, r_bar)
        Area = height * width 
        Update pointers in direction of larger area 
        '''
        l, r = 0, len(heights)-1
        maxArea = 0 

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(area, maxArea)

            # slide pointers to find a larger height
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea