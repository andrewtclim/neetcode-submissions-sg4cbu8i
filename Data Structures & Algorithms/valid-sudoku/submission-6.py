class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init hashmaps with sets {key: row_i, col_i, (sq_r_i, sq_c_i) and val: hashsets}
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # iter over each val in the board 
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # skip over empty values
                if val == '.':
                    continue 
                
                # check if val is in any hashset
                if (val in rows[r] 
                    or val in cols[c] 
                    or val in squares[(r//3, c//3)]):
                    return False
                
                # update hashset with current value
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)
        
        # passes all checks -> valid grid
        return True
