class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # top, bot  bin search 
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top+bot)//2
            pot_row = matrix[mid]
            # check the upper range of potential row
            if target > pot_row[-1]:
                # elim top part (target is larger)
                top = mid + 1
            elif target < pot_row[0]:
                bot = mid - 1
            # target is within range of pot_row -> break out of loop
            else:
                break
        
        # pointers crossed -> target is not in matrix
        if top > bot:
            return False
        
        # apply bin search to potential row
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

        

