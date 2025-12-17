from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        
        while queue:
            row_len = len(queue)
            ans = []

            for _ in range(row_len):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        result = 0
        for val in ans:
            result += val
        return result
