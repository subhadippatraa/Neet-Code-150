# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def depth(self, root):
        if root is None:
            return 0

        lh = self.depth(root.left)
        rh = self.depth(root.right)

        self.maxi = max(self.maxi, lh + rh)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root):
        self.maxi = 0
        self.depth(root)
        return self.maxi        