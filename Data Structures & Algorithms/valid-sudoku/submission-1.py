class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Input is always a 9x9 grid. We iter over each value once so O(9^2) 
        Maintain a hashset to validate uniqueness across rows, cols, squares
        Squares have a tuple pair for the square_row_i and square_col_i 

        Init hashmaps s.t.
        key: row_i, col_i, or the squares's (row_i, col_i)
        value: hashset containing value (check membership)
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # skip over any blank values
                if val == ".":
                    continue

                # check for duplicate in any of the hashsets
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    return False
                
                # update hashsets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)
        
        return True
                    