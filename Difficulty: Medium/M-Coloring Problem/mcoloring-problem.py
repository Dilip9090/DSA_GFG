class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        adj = [[] for _ in range(v)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)

        color = [0] * v

        def isSafe(node, c):
            for nei in adj[node]:
                if color[nei] == c:
                    return False
            return True

        def dfs(node):
            if node == v:
                return True

            for c in range(1, m + 1):
                if isSafe(node, c):
                    color[node] = c

                    if dfs(node + 1):
                        return True

                    color[node] = 0

            return False

        return dfs(0)