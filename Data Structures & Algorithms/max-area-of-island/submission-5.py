class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = float("-inf")
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def bfs(r, c):
            queue = [(r,c)]
            area = 0

            while queue:
                row, col = queue.pop(0)
                grid[row][col] = 0
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0
                        or nr >= ROWS or nc >= COLS
                        or grid[nr][nc] == 0):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                
                area += 1

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea if maxArea != float("-inf") else 0