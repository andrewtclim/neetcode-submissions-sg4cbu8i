class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE : O(n^2)
        res = 0

        # compute the area for each possible container 
        # first iter over every left pointer
        for l in range(len(heights)):
            # iter over each right pointer (each container wrt to current left)
            for r in range(l+1, len(heights)):
                # area = width * height 
                # width is the x-axis (how many units between l and r)
                # height here is the minimum height of the left and right bars
                area = (r-l) * min(heights[l], heights[r])
                # update your res 
                res = max(area, res)
        
        return res
        