class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize variables for the m x n matrix 
        # rows = m and cols = n
        # top = index of top subarray, bot = index of bottom subarry
        rows = len(matrix)
        cols = len(matrix[0])
        top, bot = 0, rows-1

        # find a possible row that target could be in
        while top <= bot:
            mid = (top + bot)//2 
            if target > matrix[mid][-1]:
                # eliminate top half (target is a larger number)
                top = mid+1
            elif target < matrix[mid][0]:
                # eliminate bottom half (target is a smaller number)
                bot = mid-1
            else:
                # found a possible row
                break
        
        # when the target is larger than last rows last elem or smaller than first rows smallest elem
        if not (top <= bot):
            return False
        
        # perform binary_search on the possible row
        possible_row = matrix[mid]
        # initalize index for the first and last elems in the row
        l, r = 0, cols-1
        while l <= r:
            m = (l+r)//2
            if target == possible_row[m]:
                return True
            elif target > possible_row[m]:
                l = m + 1
            else:
                r = m - 1
        # target is not in the possible row
        return False



