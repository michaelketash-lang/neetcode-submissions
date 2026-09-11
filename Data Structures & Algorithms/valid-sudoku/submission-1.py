class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                keys = [("rows",r,val),("cols",c,val),("box",r//3,c//3,val)]
                if any(k in seen for k in keys):
                    return False
                seen.update(keys)
        return True        

