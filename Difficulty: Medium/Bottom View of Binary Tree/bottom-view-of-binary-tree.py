'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []

        mp = {}
        q = deque([(root, 0)])

        while q:
            node, hd = q.popleft()

            mp[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        ans = []

        for hd in sorted(mp):
            ans.append(mp[hd])

        return ans