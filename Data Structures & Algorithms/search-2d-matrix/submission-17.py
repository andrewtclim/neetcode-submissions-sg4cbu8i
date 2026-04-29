class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search vertically for the possible row first 
        top, bot = 0, len(matrix)-1 

        while top <= bot:
            mid = (top + bot)//2
            pos_row = matrix[mid]
            if target > pos_row[-1]:
                # eliminate the top half 
                top = mid + 1
            elif target < pos_row[0]:
                # eliminate the bottom half
                bot = mid - 1
            else:
                # target is within the range between pos_row[0] to pos_row[-1]
                break

        # top and bot loop broke -> either target is too small or too big outside matrix
        if not (top <= bot):
            return False 
        
        # binary search on pos_row
        l, r = 0, len(pos_row)-1
        while l <= r:
            m = (l+r)//2
            mid = pos_row[m]
            if target == mid:
                return True 
            elif target > mid:
                l = m + 1
            else:
                r = m - 1
        
        # didnt find target...
        return False