class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        sol = 0

        def bfs(r, c):

            queue = [(r, c)]
            grid[r][c] = 0
            area = 0

            while queue:
                p_r, p_c = queue.pop(0)
                area += 1

                for dr, dc in directions:
                    nr, nc = p_r + dr, p_c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = 0

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    print(f"found area {r, c}")
                    sol = max(sol, bfs(r, c))
    
        return sol