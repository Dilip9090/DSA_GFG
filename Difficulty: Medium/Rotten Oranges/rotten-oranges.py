class Solution:
	def orangesRot(self, mat):
		# code here
		n = len(mat)
        m = len(mat[0])

        q = deque()
        fresh = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j, 0))
                elif mat[i][j] == 1:
                    fresh += 1

        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:

            r, c, t = q.popleft()
            time = max(time, t)

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        return time if fresh == 0 else -1