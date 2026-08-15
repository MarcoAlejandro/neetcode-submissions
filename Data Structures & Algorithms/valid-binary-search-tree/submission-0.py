class Solution:
    def __init__(self):
        self.is_valid = True

    def _go(self, root):
        if root is None:
            return float("inf"), float("-inf")

        left_min, left_max = self._go(root.left)
        right_min, right_max = self._go(root.right)

        if not (left_max < root.val < right_min):
            self.is_valid = False

        subtree_min = min(left_min, root.val, right_min)
        subtree_max = max(left_max, root.val, right_max)

        return subtree_min, subtree_max

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self._go(root)
        return self.is_valid