class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init hashsets for each condition 
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue 
                # check if val was in hashset -> duplicates are invalid
                if (val in rows[r]
                    or val in cols[c]
                    or val in sqs[(r//3, c//3)]):
                    return False
                
                # update hashsets
                rows[r].add(val)
                cols[c].add(val)
                sqs[(r//3, c//3)].add(val)
        
        return True