class Solution:
    def dfs(self, adj):
        # code here
        visited = [False] * len(adj)
        ans = []

        def dfsTraversal(node):
            visited[node] = True
            ans.append(node)

            for nei in adj[node]:
                if not visited[nei]:
                    dfsTraversal(nei)

        dfsTraversal(0)
        return ans