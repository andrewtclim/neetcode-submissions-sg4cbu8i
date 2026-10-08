class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top+bot)//2
            pot_row = matrix[mid]
            if target > pot_row[-1]:
                top = mid + 1
            elif target < pot_row[0]:
                bot = mid - 1
            else:
                # target within range
                break 
        
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
        
        return False