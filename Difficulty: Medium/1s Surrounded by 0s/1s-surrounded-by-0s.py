class Solution:
    def cntOnes(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            visited[r][c] = True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and
                    0 <= nc < m and
                    grid[nr][nc] == 1 and
                    not visited[nr][nc]):

                    dfs(nr, nc)

        # Traverse boundary cells
        for i in range(n):

            # First column
            if grid[i][0] == 1 and not visited[i][0]:
                dfs(i, 0)

            # Last column
            if grid[i][m - 1] == 1 and not visited[i][m - 1]:
                dfs(i, m - 1)

        for j in range(m):

            # First row
            if grid[0][j] == 1 and not visited[0][j]:
                dfs(0, j)

            # Last row
            if grid[n - 1][j] == 1 and not visited[n - 1][j]:
                dfs(n - 1, j)

        # Count enclosed 1s
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1

        return count        