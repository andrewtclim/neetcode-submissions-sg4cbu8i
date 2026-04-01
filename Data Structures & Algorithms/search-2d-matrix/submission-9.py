class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initalize vars for top and bot row indices
        top = 0
        bot = len(matrix)-1

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
        
        l, r = 0, len(possible_row)-1
        while l <= r:
            m = (l+r)//2
            midpoint = possible_row[m]
            if midpoint == target:
                return True
            elif midpoint < target:
                l = m + 1
            else:
                r = m - 1
        
        return False