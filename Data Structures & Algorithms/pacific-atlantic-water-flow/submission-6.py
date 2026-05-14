class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            queue = deque(source)

            while queue:
                row, col = queue.popleft()
                ocean[row][col] = True
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                        and ocean[nr][nc] == False
                        and heights[nr][nc] >= heights[row][col]):
                        queue.append((nr,nc))

        pacific = []
        atlantic = []

        for r in range(ROWS):
            pacific.append((r,0))
            atlantic.append((r,COLS - 1))

        for c in range(COLS):
            pacific.append((0,c))
            atlantic.append((ROWS - 1,c))
        
        bfs(atlantic, atl)
        bfs(pacific, pac)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])

        return res