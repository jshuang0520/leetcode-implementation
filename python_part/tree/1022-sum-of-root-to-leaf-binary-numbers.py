# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        refer to:
        https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/835893/python-very-easy-to-understand-runtime-beats-94-python-submissions/?orderBy=most_votes&languageTags=python

        https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/1681682/well-detailed-explaination-java-c-python-easy-for-mind-to-accept-it/?orderBy=most_votes&languageTags=python

        https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/797205/sum-root-to-leaf-binary-numbers/?orderBy=most_votes

        https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line/

        image
        https://assets.leetcode.com/users/andvary/image_1556551007.png

        --
        strategy:
        to sum and update the ans when we reach to the bottom of a leaf
        """

        def sumRootToLeaf(root, res):  # here; "res" is "sum"
            if not root:  # if root == None:
                return 0
            res = (2 * res) + root.val  # Binary to Decimal Conversion and value addition, it's similar to (12 = 10+2 = 1*10 + 2); (in binary, '11' = 1*2 + 1; and '111' = (1*2 + 1)*2 + 1 = ('11'*2) + 1 = 7), check this post: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/835893/python-very-easy-to-understand-runtime-beats-94-python-submissions/?orderBy=most_votes&languageTags=python
            if (root.left == None) and (root.right == None):  # reach to the bottom leaf
                return res
            return sumRootToLeaf(root.left, res) + sumRootToLeaf(root.right, res)

        return sumRootToLeaf(root, 0)


class Solution:
    def __init__(self):
        self.res = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:

        def traverse(root, s):
            if root:
                s += str(root.val)
                if not root.left and not root.right:
                    self.res += int(s, 2)  # Binary to Decimal Conversion and value addition
                    return
                traverse(root.left, s)
                traverse(root.right, s)
            return
        traverse(root, '')
        return self.res
