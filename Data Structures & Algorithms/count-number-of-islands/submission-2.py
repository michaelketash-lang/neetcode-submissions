class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows , cols = len(grid) , len(grid[0])
        seen = set()
        directions = [(0 , 1), ( 1, 0 ), (-1 , 0), (0 , -1)]

        def valid( r , c ):
            return (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1")


        def dfs(i , j):
            for x,y in directions:
                next_x , next_y = i + x , j + y
                if valid(next_x,next_y) and (next_x,next_y) not in seen:
                    seen.add((next_x,next_y))
                    dfs(next_x,next_y)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    islands += 1
                    seen.add((r,c))
                    dfs(r,c)
        return islands

        