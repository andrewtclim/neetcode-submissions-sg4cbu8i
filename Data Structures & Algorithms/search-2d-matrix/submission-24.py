class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # top bot binary search 
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top+bot)//2
            pot_row = matrix[mid]
            # target is larger than pot row's largest value -> elim top half
            if target > pot_row[-1]:
                top = mid + 1
            # target smaller than pot_row smallest value -> elim bot half
            elif target < pot_row[0]:
                bot = mid - 1
            # otherwise target is within pot_row's range -> keep pot row (horizontal bin search)
            else:
                break 
        
        # target is outside of range of matrix
        if top > bot:
            return False
        
        l, r = 0, len(pot_row)-1
        while l <= r:
            m = (l+r)//2
            mid = pot_row[m]
            if target == mid:
                return True 
            elif target > mid:
                l = m + 1
            else:
                r = m - 1
        
        # target not found in pot row either
        return False
