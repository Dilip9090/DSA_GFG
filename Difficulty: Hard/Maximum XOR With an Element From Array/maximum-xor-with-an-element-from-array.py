class TrieNode:
    def __init__(self):
        self.children = [None, None]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            node = node.children[bit]

    def getMaxXor(self, num):
        node = self.root
        ans = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if node.children[1 - bit]:
                ans |= (1 << i)
                node = node.children[1 - bit]
            else:
                node = node.children[bit]

        return ans
class Solution:
    def maxXor(self, arr, queries):
        # Code here
        arr.sort()

        offline = []
        for i, (x, m) in enumerate(queries):
            offline.append((m, x, i))

        offline.sort()

        trie = Trie()
        ans = [-1] * len(queries)

        idx = 0
        n = len(arr)

        for m, x, qi in offline:
            while idx < n and arr[idx] <= m:
                trie.insert(arr[idx])
                idx += 1

            if idx == 0:
                ans[qi] = -1
            else:
                ans[qi] = trie.getMaxXor(x)

        return ans
        