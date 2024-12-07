# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


def bianli(node: Optional[TreeNode]):
    if node == None:
        return
    print(node.val)
    bianli(node.left)
    bianli(node.right)


root = [3, 9, 20, None, None, 15, 7]
node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)

node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

# bianli(node)

print(Solution().maxDepth(node))
