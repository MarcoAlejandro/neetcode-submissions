# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        elems = deque()
        asnwer = []
        elems.append((root, 0))
        
        while elems:
            next_node, level = elems.popleft()
            if not next_node:
                continue
            elems.append((next_node.left, level+1))
            elems.append((next_node.right, level+1))

            if level >= len(asnwer):
                asnwer.append([])
            asnwer[level].append(next_node.val)
        
        return asnwer



        
