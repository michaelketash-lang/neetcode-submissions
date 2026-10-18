class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])

        islands = 0
        DIRS =[[0,1],[0,-1],[1,0],[-1,0]]
        visit = set()

        def valid(r , c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == "1"
        
        def dfs(r , c):
            for dx,dy in DIRS:
                nr , nc = dx + r , dy + c
                if (nr,nc) not in visit and valid(nr,nc):
                    visit.add((nr,nc))
                    dfs(nr,nc)
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visit and grid[i][j] == "1":
                    islands += 1
                    visit.add((i,j))
                    dfs(i,j)
        
        return islands