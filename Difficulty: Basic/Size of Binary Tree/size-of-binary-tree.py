"""
Definition for Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def getSize(self, root):
        # Base case
        if root is None:
            return 0
        
        # Count current node + left subtree + right subtree
        return 1 + self.getSize(root.left) + self.getSize(root.right)