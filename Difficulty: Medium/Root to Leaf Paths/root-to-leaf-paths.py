"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

from collections import deque
class Solution:
    def Paths(self, root):
        # code here
        ans = []

        def dfs(node, path):
            if not node:
                return

            path.append(node.data)

            if not node.left and not node.right:
                ans.append(path[:])
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return ans