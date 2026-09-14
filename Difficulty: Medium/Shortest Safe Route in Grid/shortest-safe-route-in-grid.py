class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])

        safe = [[1] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = 0
                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = 0

        q = []

        for i in range(n):
            if safe[i][0]:
                q.append((i, 0, 1))
                safe[i][0] = 0

        front = 0

        while front < len(q):
            i, j, d = q[front]
            front += 1

            if j == m - 1:
                return d

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < m and safe[ni][nj]:
                    safe[ni][nj] = 0
                    q.append((ni, nj, d + 1))

        return -1        