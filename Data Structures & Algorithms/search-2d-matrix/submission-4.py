class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize variables for rows and cols (m x n)
        rows, cols = len(matrix), len(matrix[0])
        # initalize bin_search variables for top and bottom indicies
        top, bot = 0, len(matrix)-1

        # bin search to find a possible row
        while top <= bot:
            mid = (top + bot)//2
            possible_row = matrix[mid]
            if target > possible_row[-1]:
                # lower the top (target is closer to bot)
                top = mid + 1
            elif target < possible_row[0]:
                # raise the bot (target closer to top)
                bot = mid - 1
            else:
                # found a target that is within the range of possible row 
                break
        
        # loop kept continuing and is beyond scope of matrix
        if not (top <= bot):
            return False
        
        # commit bin_search on possible_row
        l, r = 0, len(possible_row)-1
        while l <= r:
            m = (l+r)//2
            if target == possible_row[m]:
                return True
            elif target > possible_row[m]:
                l = m + 1
            else:
                r = m - 1
        
        return False
