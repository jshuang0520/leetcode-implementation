from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        refer to: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/solutions/252722/python-stack-solution-beats-100-on-runtime-and-memory/?orderBy=most_votes&languageTags=python

        First item in preorder list is the root to be considered.
        For next item in preorder list, there are 2 cases to consider:
            If value is less than last item in stack, it is the left child of last item.
            If value is greater than last item in stack, pop it.
                The last popped item will be the parent and the item will be the right child of the parent.
        """
        root_val = preorder[0]
        root = TreeNode(root_val)

        # TODO - read this: https://stackoverflow.com/questions/64840443/appending-nodes-of-tree-to-a-python-list
        stack = [root]  # this stack stores: a list of TreeNode, something like below
        '''
                 A 
              /  |   \
            B    C    D
          /  \   |   / | \
         E    F  G  H  I  J
         
        may collect it into this form -> [[A], [B, C, D], [E, F, G, H, I, J]]
        '''

        for value in preorder[1:]:
            if value < stack[-1].val:  # the 'top' of this stack is a potential 'parent node' for TreeNode
                stack[-1].left = TreeNode(value)  # n1 = Node(1), n2 = Node(2) ---> n1.left = n2, currently stack[-1] is our root node
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root
