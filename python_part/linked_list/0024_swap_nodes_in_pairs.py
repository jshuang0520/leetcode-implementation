# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
Linked List
0024	Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


# Time:  O(n)
# Space: O(1)


# Definition for singly-linked list.
class ListNode:
    """
    reference
    --
    combine the following parts:

    1. sample code in this topic
    https://leetcode.com/problems/merge-two-sorted-lists/

    2. google: python create a linked list stack overflow
    https://stackoverflow.com/questions/52706232/linked-list-python

    class LinkedList:
        def __init__(self, item=None):
            self.next = None
            self.val = item

        def __len__(self):
            cur = self
            count = 1 if self.val is not None else 0
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count

        def append(self, item):
            if not self.val:
                self.val = item
                return

            cur = self
            while cur.next is not None:
                cur = cur.next
            cur.next = LinkedList(item)
    """

    # def __init__(self, x):
    #     self.val = x
    #     self.next = None

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        cur = self
        count = 1 if self.val is not None else 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

    def append(self, item):
        if not self.val:
            self.val = item
            return

        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(item)


def create_linked_list(input_list):
    linked_list = ListNode()
    for elem in input_list:
        linked_list.append(elem)
    return linked_list


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @staticmethod
    def run(head: ListNode) -> ListNode:
        """
        reference

        google: python Intersection of Two Linked Lists
        https://zhenyu0519.github.io/2020/06/07/lc160/#example-3
        --

        Runtime: 164 ms, faster than 53.70% of Python3 online submissions for Intersection of Two Linked Lists.
        Memory Usage: 29.2 MB, less than 91.34% of Python3 online submissions for Intersection of Two Linked Lists.
        """
        dummy = ListNode(0)  # TODO: unable to think of this part
        dummy.next = head    # TODO: unable to think of this part
        current = dummy      # TODO: unable to think of this part
        while head.next and head.next.next:  # TODO: unable to think of this part
            one, two, three, four = current.val, current.next, current.next.next, current.next.next.next
            current.val = two
            current.next = one
            current.next.next = four  # FIXME: ERROR this line
            '''
            AttributeError: 'int' object has no attribute 'next'
                current.next.next = four
            Line 15 in swapPairs (Solution.py)
                ret = Solution().swapPairs(param_1)
            Line 41 in _driver (Solution.py)
                _driver()
            Line 52 in <module> (Solution.py)
            '''
            current.next.next.next = three
        return dummy.next

    @staticmethod
    def run_2(head: ListNode) -> ListNode:
        """
        dummy: 0 -> None
        dummy: 0 -> ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
        """
        dummy = ListNode(0)
        print('dummy:', dummy.__repr__())  # dummy: 0 -> None
        dummy.next = head
        print('head:', head.__repr__())  # head: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
        print('dummy:', dummy.__repr__())  # dummy: 0 -> ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
        current = dummy
        print('current.val:', current.val)  # current.val: 0
        print('current.next:', current.next)  # current.next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
        # current can be seen as:
        # val -next-> (linked list)
        # (0)    ->   (1 -> 2 -> 3 -> 4)
        # (0) in the very beginning is because of ListNode(0), -the_next_linked_list_is-> (the given param: head)
        print('head.next:', head.next)  # head.next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
        # head.val == 1,
        # head.next ==      ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
        # head.next.next == ListNode{val: 3, next: ListNode{val: 4, next: None}}

        # TODO: to see the whole picture
        # current: 0 -> ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
        # current.val: 0
        # current.next:           ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
        # current.next.next:                             ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
        # current.next.next.next:                                               ListNode{val: 3, next: ListNode{val: 4, next: None}
        # turn '(0) -> (1 -> 2 -> 3 -> 4)' into '(0) -> (2 -> 1 -> 4 -> 3)'
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            # FIXME: can't figure it out (the code below) - guess: 他只關注前兩個要怎麼改變鏈結方式而已。之所以不是期望的 next_four 是因為這邊很 tricky，他不打算一次處理4個，前2個弄完(對調完)之後，他要 link 的是下一組 pair，也就是第3個，所以會看到 next_one.next = next_three 之後又接 current = next_one
            next_one.next = next_three
            current = next_one

if __name__ == '__main__':
    sol = Solution()
    print(sol.run(head_a=create_linked_list([4, 1, 8, 4, 5]), head_b=create_linked_list([5, 6, 1, 8, 4, 5])))
    # print(sol.run(head_a=create_linked_list([1, 9, 1, 2, 4]), head_b=create_linked_list([3, 2, 4])))
    # FIXME: I failed to reproduce the act of two linked list, so the answer showed in pycharm is wrong (but it is correct in leetcode)
