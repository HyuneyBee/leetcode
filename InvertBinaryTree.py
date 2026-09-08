from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node:
                if node.left or node.right:
                    node.left, node.right = node.right, node.left

                q.append(node.right)
                q.append(node.left)

        return root

