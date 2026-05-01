class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init vertical binary search 
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top+bot)//2
            pos_row = matrix[mid]
            # elim top half (small numbers)
            if target > pos_row[-1]:
                top = mid + 1
            # elim bot half (large numbers)
            elif target < pos_row[0]:
                bot = mid - 1
            else:
                break # found our possible row to search 
        
        # if the loop breaks (target is beyond matrix) -> return False
        if not (top <= bot):
            return False
        
        # run binary search on possible row
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
        
        # didnt find target
        return False
