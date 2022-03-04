# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        queue = []
        if not root:
            return []
        queue.append(root)
        while len(queue)>0:
            Sum = 0
            length = len(queue)
            for i in range(length):
                curr_node = queue.pop(0)
                Sum += curr_node.val
                if(curr_node.left):
                    queue.append(curr_node.left)
                if(curr_node.right):
                    queue.append(curr_node.right)
            averages.append(Sum/length)
        return averages