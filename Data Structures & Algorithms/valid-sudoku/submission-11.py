class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init hashsets for each type of group 
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        # iter over each value in the the board
        for r in range(9):
            for c in range(9):
                # init val 
                val = board[r][c]

                # skip empty values
                if val == ".":
                    continue 
                
                # check duplicate values
                if (val in rows[r] or val in cols[c] or val in sqs[(r//3, c//3)]):
                    return False
                
                # update hashsets
                rows[r].add(val)
                cols[c].add(val)
                sqs[(r//3, c//3)].add(val)
        
        return True
