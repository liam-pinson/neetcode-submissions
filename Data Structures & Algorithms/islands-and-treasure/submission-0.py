import sys

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])

        map_ = []

        def bfs(r, c):

            queue = [(r, c)]
            nearest = 0
            length = 0
            visited = set()
            visited.add((r,c))

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.pop(0)
                    if grid[row][col] == 0:
                        return length

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if ((nr, nc) in visited 
                            or nr < 0 or nc < 0 
                            or nr >= ROWS or nc >= COLS 
                            or grid[nr][nc] == -1):
                            continue
                        else:
                            queue.append((nr, nc))
                            visited.add((nr, nc))

                length += 1

                # if length == 3:
                #     break

            return length


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    print(r, c)
                    grid[r][c] = bfs(r, c)
        return