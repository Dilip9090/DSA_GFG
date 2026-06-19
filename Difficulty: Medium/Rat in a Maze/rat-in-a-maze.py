class Solution:
    def ratInMaze(self, maze):
        # code here
        n = len(maze)

        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []

        ans = []
        visited = [[False] * n for _ in range(n)]

        # D, L, R, U for lexicographical order
        directions = [
            (1, 0, 'D'),
            (0, -1, 'L'),
            (0, 1, 'R'),
            (-1, 0, 'U')
        ]

        def dfs(r, c, path):
            if r == n - 1 and c == n - 1:
                ans.append(path)
                return

            visited[r][c] = True

            for dr, dc, move in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < n and
                    maze[nr][nc] == 1 and
                    not visited[nr][nc]):
                    dfs(nr, nc, path + move)

            visited[r][c] = False  # backtrack

        dfs(0, 0, "")
        return ans