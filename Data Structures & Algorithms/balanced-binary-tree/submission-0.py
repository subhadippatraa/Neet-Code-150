class Solution:
    def depth(self, root) -> int:
        if root is None:
            return 0

        lh = self.depth(root.left)
        if lh == -1:
            return -1

        rh = self.depth(root.right)
        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root) != -1