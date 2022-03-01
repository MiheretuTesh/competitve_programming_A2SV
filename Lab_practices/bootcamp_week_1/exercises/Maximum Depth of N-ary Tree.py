"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node, depth):
            if not node.children:
                return depth
            depth += 1
            max_val = 0
            for i in node.children:
                a = dfs(i, depth)
                max_val = max(a, max_val)
            return max_val
        return dfs(root, 1) if root else 0