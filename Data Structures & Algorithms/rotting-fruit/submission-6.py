class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh = 0
        queue = deque([])
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        while fresh > 0 and queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                        and grid[nr][nc] == 1):
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            
            time += 1

        return time if fresh == 0 else -1