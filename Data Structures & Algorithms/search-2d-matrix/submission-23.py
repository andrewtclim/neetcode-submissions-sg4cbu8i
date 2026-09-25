class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        one loop bineary search scan 
        here the midpoint is defined by two indicies (its row and column)
        mid_row = mid // n (the row that its in is the midpoint divided num_of_rows)
        mid_col = mid % m (the col its in is the midpoint modulo num_of_cols)

        Row (via // n): "how many rows have I completely walked through?"
        Col (via % n): "how far am I into the current row?

        '''
        # init row and col variables 
        m = len(matrix)
        n = len(matrix[0])

        # init binary search pointers
        l = 0 
        r = (m*n)-1

        while l <= r:
            mid = (l+r)//2
            # locate the indicies for the respective row and col (flat index logic)
            mid_row = mid // n
            mid_col = mid % n 
            # calc the midpoint 
            midpoint = matrix[mid_row][mid_col]
            if target == midpoint:
                return True
            # target large so elim bottom half
            elif target > midpoint:
                l = mid + 1
            # the opposite
            else:
                r = mid - 1
        
        # after scanning didnt find target 
        return False


