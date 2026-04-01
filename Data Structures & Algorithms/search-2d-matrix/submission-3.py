class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize vars for the rows and cols 
        rows, cols = len(matrix), len(matrix[0])

        # initalize pointers for top and bottom row
        top, bot = 0, len(matrix)-1

        # loop to find possible row 
        while top <= bot:
            mid = (top + bot)//2
            possible_row = matrix[mid]
            if target > possible_row[-1]:
                # lower the roof (target is located at bottom (higher))
                top = mid + 1
            elif target < possible_row[0]:
                # raise the floor (target is located near top (lower num))
                bot = mid - 1
            else:
                # found a possible row -> leave loop 
                break 
        
        # if the possible row wasnt found with loop (either its too big or small)
        if not (top <= bot):
            return False
        
        # binary search on possible row
        l, r = 0, len(possible_row)-1
        while l <= r:
            m = (l+r)//2
            if target == possible_row[m]:
                return True
            elif target > possible_row[m]:
                l = m + 1
            else:
                r = m - 1

        # not found in possible row
        return False

            