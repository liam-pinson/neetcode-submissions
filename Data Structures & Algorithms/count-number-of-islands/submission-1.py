class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        
        def bfs(r,c):
            queue = [(r,c)]
            grid[r][c] = "0"

            while queue:
                row, col = queue.pop(0)
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"

            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands
        
