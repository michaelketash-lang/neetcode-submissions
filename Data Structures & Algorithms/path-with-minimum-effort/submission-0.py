class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRS = [[1,0], [-1,0] , [0,-1] , [0,1]]
        ROWS = len(heights)
        COLS = len(heights[0])
        best = [[float('inf')]*COLS for i in range(ROWS)]
        best[0][0] = 0

        heap = [(0 , 0 , 0)]
        def valid(r , c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS

        while heap:
            effort , r , c = heapq.heappop(heap)

            if r == ROWS - 1 and c == COLS - 1:
                return effort
            
            if effort > best[r][c]:
                continue
            
            for dr , dc in DIRS:
                nr , nc = r + dr , c + dc

                if valid(nr,nc):
                    new_effort = max(effort , abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < best[nr][nc]:
                        best[nr][nc] = new_effort
                        heapq.heappush(heap , (new_effort , nr , nc))
        
