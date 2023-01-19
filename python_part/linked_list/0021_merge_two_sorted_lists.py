from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = temp = ListNode(0)
        while l1 != None and l2 != None:  # 1

            if l1.val < l2.val:  # 2
                temp.next = l1  # 3
                l1 = l1.next  # 4
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  # 5
        return dummy.next  # 6
print(Solution.mergeTwoLists(None, l1=[1,2,4], l2=[1,3,4]))

# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
Linked List
0021	Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

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
        cur.next = ListNode(item)


def create_linked_list(input_list):
    linked_list = ListNode()
    for elem in input_list:
        linked_list.append(elem)
    return linked_list


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    def run(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        description

        Merge two sorted 'linked lists' and return it as a sorted list.
        The list should be made by 'splicing together' the 'nodes' of the first two lists.
        -> 'nodes' - node ; 'splicing together' - relationship (that is 'linked')
        -> linked list
        --
        Your Input
        l1 = [1,2,4]
        l2 = [1,3,4]

        stdout
        l2: ListNode{val: 3, next: ListNode{val: 4, next: None}}
        l1: ListNode{val: 2, next: ListNode{val: 4, next: None}}
        l1: ListNode{val: 4, next: None}
        l2: ListNode{val: 4, next: None}
        l2: None
        dummy: <__main__.ListNode object at 0x7fe0d13765e0>
        dummy.val: 0
        dummy.next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}}
        --
        curr: ListNode{val: 4, next: ListNode{val: 4, next: None}}
        curr.val: 4
        curr.next: ListNode{val: 4, next: None}

        Runtime: 40 ms, faster than 43.14% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14.2 MB, less than 60.45% of Python3 online submissions for Merge Two Sorted Lists.
        """
        # tmp = l1.extend(l2)
        # return sorted(tmp)

        # FIXME: I was not familiar with the usage of linked lists in python - need .val, .next
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                # self.logger.info('l1: {}'.format(l1))
                # print('l1:', l1.__repr__)
                # self.logger.info('curr.val: {}'.format(curr.val))
                # self.logger.info('curr.__repr__: {}'.format(curr.__repr__))
            else:
                curr.next = l2
                l2 = l2.next
                # self.logger.info('l2: {}'.format(l2))
                # self.logger.info('curr.val: {}'.format(curr.val))
                # self.logger.info('curr.__repr__: {}'.format(curr.__repr__))
            curr = curr.next
            self.logger.info('curr.__repr__(): {}'.format(curr.__repr__()))
            self.logger.info('dummy.__repr__(): {}'.format(dummy.__repr__()))
        curr.next = l1 or l2
        # self.logger.info('dummy: {}'.format(dummy))
        # self.logger.info('dummy.val: {}'.format(dummy.val))
        # self.logger.info('dummy.next: {}'.format(dummy.next))
        # self.logger.info('--')
        # self.logger.info('curr: {}'.format(curr))
        # self.logger.info('curr.val: {}'.format(curr.val))
        # self.logger.info('curr.next: {}'.format(curr.next))
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(l1=create_linked_list([1, 2, 4]), l2=create_linked_list([1, 3, 4])))
    print(sol.run(l1=create_linked_list([]), l2=create_linked_list([0])))
    # print('\n')
    # a = create_linked_list([1, 2, 4])
    # b = a
    # print(len(a))
    # print('--')
    # for i in range(0, len(a)):
    #     print(a.val)
    #     a = a.next
    # print(b.next)

