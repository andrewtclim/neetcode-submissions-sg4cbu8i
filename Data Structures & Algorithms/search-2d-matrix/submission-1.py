class Solution:
    def searchMatrix(self, matrix, target):
        # define vars for the m x n matrix
        rows, cols = len(matrix), len(matrix[0])
        # initalize index pointers for the top and bottom rows 
        top, bot = 0, rows-1

        # binary search on the rows of the matrix -> locate possible row OR target is beyond the limits  
        # mid (the middle index) will be the index of the possible row (if it exists)
        while top <= bot:
            mid = (top + bot)//2
            if target > matrix[mid][-1]:
                # eliminate top half 
                top = mid + 1
            elif target < matrix[mid][0]:
                # eliminate bottom half
                bot = mid - 1
            else:
                # found a possible row
                # target is within the bounds of matrix[mid]
                break
    
        # when the target larger than highest value or smallest than smallest value
        if not (top <= bot):
            return False
    
        # binary search on the possible row that was found earlier 
        possible_row = matrix[mid]
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


