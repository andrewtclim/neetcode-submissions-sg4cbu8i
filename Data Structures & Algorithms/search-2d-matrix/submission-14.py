class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search vertically on the rows of the matrix
        top, bot = 0, len(matrix)-1

        while top <= bot:
            # find middle row 
            mid = (top+bot)//2
            possible_row = matrix[mid]
            # eliminate top half (small numbers)
            if target > possible_row[-1]:
                top = mid + 1
            elif target < possible_row[0]:
                bot = mid - 1
            else:
                # found a possible row (range)
                break
        
        if not (top <= bot):
            return False
        
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
        
        return False