from collections import defaultdict
ROWS = 9
COLS = 9
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # save a hashset for rows
        rows = defaultdict(set)
        # save a hashset for cols
        cols = defaultdict(set)
        # save hashset for both that the key is (r//3,c//3)
        squared = defaultdict(set)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in rows[row] or
                    board [row][col] in cols[col] or
                    board[row][col] in squared[(row//3,col//3)]):
                    #there is a duplicate so:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squared[(row//3,col//3)].add(board[row][col])

        return True