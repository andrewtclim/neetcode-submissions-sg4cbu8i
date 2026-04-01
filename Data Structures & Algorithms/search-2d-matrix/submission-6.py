class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize row and cols var
        rows, cols = len(matrix), len(matrix[0])

        # initalize binary search pointers for top and bot row
        top, bot = 0, len(matrix)-1

        # binary search vertically to find a possible row that target could be in 
        while top <= bot:
            # find middle index -> potential row
            mid = (top+bot)//2
            possible_row = matrix[mid]
            if target > possible_row[-1]:
                # target is large (eliminate top half)
                top = mid + 1
            elif target < possible_row[0]:
                # target is small (eliminate bottom half)
                bot = mid - 1
            else:
                # found a row where target is between the range 
                break 
        
        # target not found in matrix range (loop keeps continuing)
        if not (top <= bot):
            return False

        # perform binary search on possible row
        l, r = 0, len(possible_row)-1
        while l <= r:
            m = (l+r)//2
            midpoint = possible_row[m]
            if target == midpoint:
                return True
            elif target > midpoint:
                l = m + 1
            else:
                r = m - 1
        
        # loop continues (not found in possible row)
        return False
