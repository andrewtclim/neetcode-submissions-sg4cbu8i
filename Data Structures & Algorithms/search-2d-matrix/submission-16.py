class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init pointers for bin search vertically 
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot)//2
            pos_row = matrix[mid]
            # target is larger than middle rows largest value -> elim top half (ascend)
            if target > pos_row[-1]:
                top = mid + 1
            elif target < pos_row[0]:
                bot = mid - 1
            # otherwise target is inside pos_row (we will search this)
            else:
                break
        
        # target is either way too big or small outside of matrix 
        if not (top <= bot):
            return False
        
        # binary search on pos_row
        l, r = 0, len(pos_row)-1
        while l <= r:
            m = (l+r)//2
            if target == pos_row[m]:
                return True
            elif target > pos_row[m]:
                l = m + 1
            else:
                r = m - 1
        
        # when not found in pos_row -> False
        return False
