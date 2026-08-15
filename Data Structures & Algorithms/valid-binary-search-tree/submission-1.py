# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self._is_valid = True

    def _go(self, root: Optional[TreeNode]) -> list:
        if root is None:
            return float("inf"), float("-inf")

        left_min, left_max = self._go(root.left)
        right_min, right_max = self._go(root.right)

        if not (left_max < root.val < right_min):
            self._is_valid = False

        return min(left_min, root.val, right_min), max(left_max, root.val, right_max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self._go(root)
        return self._is_valid
        