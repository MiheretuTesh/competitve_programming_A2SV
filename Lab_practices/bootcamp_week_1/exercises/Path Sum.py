# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_val = 0
        def dfs(node, sum_val):
            sum_val += node.val
            if node.left == None and node.right == None:
                if sum_val == targetSum:
                    return True
                else:
                    return False
            elif node.left and node.right == None:
                return dfs(node.left, sum_val)
            elif node.right and node.left == None:
                return dfs(node.right, sum_val)
            else:
                return dfs(node.left, sum_val) or dfs(node.right, sum_val)
        return dfs(root, sum_val) if root else False
    