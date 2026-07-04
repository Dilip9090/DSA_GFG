'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        if not root:
            return []

        mp = {}
        q = deque([(root, 0)])

        while q:
            node, hd = q.popleft()

            if hd not in mp:
                mp[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        ans = []

        for hd in sorted(mp):
            ans.append(mp[hd])

        return ans
        