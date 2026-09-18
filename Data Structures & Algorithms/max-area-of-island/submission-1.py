class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # first- intializations:
        seen = set() # track the (row,col) we visited
        rows , cols = len(grid) , len(grid[0])
        max_area = 0 # track the maximum area
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        # need to check if (row,col) is valid
        # valid means : row is [0,rows) , col is [0,cols), grid[row][col]= "1"
        def valid (r , c):
            return (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1)
        
        # will return the area of the island
        def dfs(r , c):
            nonlocal count
            count += 1
            for x,y in directions:
                next_r , next_c = r + x , c + y
                if valid(next_r,next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    dfs(next_r,next_c)
                
            return count
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    count = 0
                    dfs(r,c)
                    max_area = max(max_area,count)
        
        return max_area
        
