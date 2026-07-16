class Solution:
    def bfs(self, adj):
        # code here
        visited = [False] * len(adj)
        ans = []
        q = deque([0])

        visited[0] = True

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return ans