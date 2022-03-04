# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zig = False
        queue = [[root.val]]
        q = [root]
        while q:
            for _ in range(len(q)):
                current = q.pop(0)
                if current:
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)
            queue.append([x.val for x in q])
        queue.pop()
        for i in range(len(queue)):
            if i%2 != 0:
                queue[i] = queue[i][::-1]
        return queue