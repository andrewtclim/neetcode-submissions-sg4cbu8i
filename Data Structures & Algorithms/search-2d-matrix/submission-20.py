class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first do bin search from top to bot (search for a potential row)
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot)//2
            pot_row = matrix[mid]
            # if the target is above the last pot row value -> elim top half
            if target > pot_row[-1]:
                top = mid + 1
            # target is smaller than the pot rows smallest value -> elim bot half
            elif target < pot_row[0]:
                bot = mid - 1
            # otherwise the target can be in the range of the pot_row 
            else:
                break 
        
        if top > bot:
            return False

        # apply binary search on potential row 
        l, r = 0, len(pot_row)-1
        while l <= r:
            m = (l+r)//2
            if target == pot_row[m]:
                return True
            elif target > pot_row[m]:
                l = m + 1
            else:
                r = m - 1
        
        # didnt find in our bin search on pot_row -> return False
        return False 

