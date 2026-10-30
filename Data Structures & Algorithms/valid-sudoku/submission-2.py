class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        combine = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                cell = board[r][c]
                if (cell in rows[r] or cell in cols[c] or board[r][c] in combine[(r//3 , c // 3)]):
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                combine[(r//3,c//3)].add(cell)
        
        return True

                
