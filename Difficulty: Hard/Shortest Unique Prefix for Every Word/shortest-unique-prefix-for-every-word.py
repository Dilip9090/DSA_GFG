class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def findPrefixes(self, arr):
        # code here
        root = TrieNode()

        for word in arr:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1

        ans = []
        for word in arr:
            node = root
            prefix = ""
            for ch in word:
                node = node.children[ch]
                prefix += ch
                if node.count == 1:
                    break
            ans.append(prefix)

        return ans