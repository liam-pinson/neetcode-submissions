class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def find_size(r, c):
            queue = [(r,c)]
            size = 0
            visited.add((r,c))

            while queue:
                print(queue)
                row, col = queue.pop(0)

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0
                        or nr >= ROWS or nc >= COLS
                        or grid[nr][nc] == 0):
                        size += 1
                    elif (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return size


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return find_size(r, c)
        return 0