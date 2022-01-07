# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = collections.defaultdict(list)
        def _helper(root, level):
            if not root: return None
            self.result[level] += [root.val]
            _helper(root.left, level + 1)
            _helper(root.right, level + 1)
            
        _helper(root, 0)
        return map(lambda (idx, x): reversed(x) if idx & 1 else x, enumerate(self.result.values()))