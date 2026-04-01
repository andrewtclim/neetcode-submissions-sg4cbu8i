class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize vars for rows and cols 
        rows, cols = len(matrix), len(matrix[0])

        # binary search vertically to find possible row 
        top, bot = 0, len(matrix)-1

        # binary search will update top and bot 
        # if it finds an appropriate row -> store possible_row
        # if loop keeps continuing (target is beyond scope of matrix)

        while top <= bot:
            mid = (top + bot)//2
            possible_row = matrix[mid]
            if target > possible_row[-1]:
                top = mid + 1
            elif target < possible_row[0]:
                bot = mid - 1
            else:
                # found potential row 
                break
        
        # target outside of matrix
        if not (top <= bot):
            return False
        
        # binary search on possible row
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
        
        # cant find in possible_row either
        return False