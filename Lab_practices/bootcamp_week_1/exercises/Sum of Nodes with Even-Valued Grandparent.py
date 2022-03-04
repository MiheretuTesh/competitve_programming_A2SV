# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        parents = dict()
        def dfs(root, start):
            if not root:
                return 0
            parents[root]=start
            if start and parents[start] and (parents[start].val%2==0):
                self.res += root.val
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, 0)
        return self.res