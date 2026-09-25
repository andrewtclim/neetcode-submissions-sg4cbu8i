class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # two seperate loop solution O(log m) and O(log n)
        # first search for a potential row (vertical search)
        top, bot = 0, len(matrix)-1
        while top <= bot:
            mid = (top+bot)//2
            pot_row = matrix[mid]
            # target is smaller (elim bot half)
            if target < pot_row[0]:
                bot = mid - 1
            # target bigger (elim top half)
            elif target > pot_row[-1]:
                top = mid + 1
            # otherwise we found a potential target
            else:
                break 
        
        # scanned all rows -> didnt find any potential rows
        if top > bot:
            return False

        # binary search on potential row 
        l, r = 0, len(pot_row)-1
        while l <= r:
            m = (l+r)//2
            midpoint = pot_row[m]
            if midpoint == target:
                return True
            # elim left half (target larger)
            elif target > midpoint:
                l = m + 1
            else:
                r = m - 1
        
        # otherwise didnt find in potential row -> no target found 
        return False

