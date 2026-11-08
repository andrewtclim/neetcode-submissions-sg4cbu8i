class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set) # square index = (r//3, c//3)

        # iter over rows
        for r in range(9):
            # iter over cols
            for c in range(9):
                val = board[r][c]

                # skip any empty values
                if val == ".":
                    continue

                if (val in rows[r] or val in cols[c] or val in sqs[(r//3, c//3)]):
                    return False
                
                # update hashsets
                rows[r].add(val)
                cols[c].add(val)
                sqs[(r//3, c//3)].add(val)
        
        return True
                
