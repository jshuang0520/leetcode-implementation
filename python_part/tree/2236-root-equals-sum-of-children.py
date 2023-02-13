# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime 33 ms Beats 70.77% Memory 13.8 MB Beats 92.39%
        """
        return root.val == root.left.val + root.right.val


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime 36 ms Beats 53.84% Memory 13.9 MB Beats 42.35%
        """
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False


class Solution:
    """
    Runtime Error
    TypeError: unsupported operand type(s) for +: 'TreeNode' and 'TreeNode'
    """
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left + root.right:
            return True
        else:
            return False
