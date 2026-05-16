class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search vertically first 
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot)//2
            pos_row = matrix[mid]
            # elim top half
            if target > pos_row[-1]:
                top = mid + 1
            # elim bot half, target smaller
            elif target < pos_row[0]:
                bot = mid - 1
            # potential row exists (target within boundaries)
            else:
                break 
        
        # target is either too large or too small 
        if not top <= bot:
            return False

        # perform binary search on pos_row
        l, r = 0, len(pos_row)-1
        while l <= r:
            m = (l+r)//2
            mid = pos_row[m]
            if mid == target:
                return True
            elif target > mid:
                l = m + 1
            else:
                r = m - 1 
        
        return False
