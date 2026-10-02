class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init bin search top to bot
        top, bot = 0, len(matrix)-1

        while top <= bot:
            m = (top+bot)//2
            pot_row = matrix[m]
            # target is larger than pot row's largest (elim top half)
            if target > pot_row[-1]:
                top = m + 1
            elif target < pot_row[0]:
                bot = m - 1
            # otherwise target is in range of pot_row
            else:
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
        
        # none found
        return False