class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize bin search pointers for possible row 
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top+bot)//2
            possible_row = matrix[mid]
            if target > possible_row[-1]:
                top = mid + 1
            elif target < possible_row[0]:
                bot = mid - 1
            else:
                break 
        
        if not (top <= bot):
            return False
        
        l, r = 0, len(possible_row)
        while l <= r:
            m = (l+r)//2
            if target == possible_row[m]:
                return True
            elif target > possible_row[m]:
                l = m + 1
            else:
                r = m - 1
        
        return False