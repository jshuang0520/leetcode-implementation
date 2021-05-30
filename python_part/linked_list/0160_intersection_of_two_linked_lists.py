# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
Linked List
0160	Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Time:  O(m + n)
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

    def run(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        # # FIXME: can't examine those two linked list parallelly, otherwise, one can't find the intersection node
        # cnt = 0
        # while headA.next and headB.next:
        #     print('headA.val:', headA.val)
        #     print('headB.val:', headB.val)
        #     if headA.val != headB.val:
        #         headA = headA.next
        #         headB = headB.next
        #         cnt += 1
        #     else:
        #         return 'Intersected at "{}"'.format(headA.val)
        #     print('headA.__repr__:', headA.__repr__)
        #     print('headB.__repr__:', headB.__repr__)

        # # FIXME: mistake - there might be multiple elements that are the intersection of these two linked lists, so don't try to use intersection of dictionaries to find the answer, that doesn't help
        # cur_a, cur_b = head_a, head_b
        # set_A = set()
        # for i in range(0, head_a.__len__()):
        #     set_A.add(cur_a.val)
        #     cur_a = cur_a.next
        # print(set_A)

        # solution
        """
        Runtime: 164 ms, faster than 53.70% of Python3 online submissions for Intersection of Two Linked Lists.
        Memory Usage: 29.6 MB, less than 27.44% of Python3 online submissions for Intersection of Two Linked Lists.
        --

        Execution log on leetcode

        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}}>
        =====
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 6, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 4, next: ListNode{val: 5, next: None}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 5, next: None}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 4, next: ListNode{val: 5, next: None}}>
        --
        cur_a.__repr__: <method-wrapper '__repr__' of NoneType object at 0x955c90>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 5, next: None}>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}}>
        cur_b.__repr__: <method-wrapper '__repr__' of NoneType object at 0x955c90>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 6, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}>
        --
        cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}>
        cur_b.__repr__: <bound method ListNode.__repr__ of ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}>
        --
        final cur_a.__repr__: <bound method ListNode.__repr__ of ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}>
        """
        cur_a, cur_b = head_a, head_b  # TODO: unable to think of this part
        # self.logger.info('cur_a.__repr__(): {}:'.format(cur_a.__repr__()))
        # self.logger.info('cur_b.__repr__(): {}:'.format(cur_b.__repr__()))
        # print('=====')

        while cur_a != cur_b:  # TODO: unable to think of this part
            cur_a = cur_a.next if cur_a else cur_b  # TODO: unable to think of this part - we loop and compare both of the linked lists, 在 intersection node 之前差多少 node，這個 loop 就會重複幾次。精髓在於 (1)一邊 linked list 走完就要交替走，拿另一個 linked list 來繼續走  (2)cur_a, cur_b 其中一個比較短的 linked list loop 到底的話，他會先走到 None，但是另一個 linked list 還會繼續 loop，這時候就會消除 1 個「在 intersection node 之前差多少 node」的差距，直到有一天消除完所有差距，就會一起（同時）走到 intersection node
            # self.logger.info('cur_a.__repr__(): {}:'.format(cur_a.__repr__()))
            cur_b = cur_b.next if cur_b else cur_a
            # self.logger.info('cur_b.__repr__(): {}:'.format(cur_b.__repr__()))
            # print('--')
        # self.logger.info('final cur_a.__repr__(): {}:'.format(cur_a.__repr__()))
        return cur_a  # TODO: unable to think of this part


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(head_a=create_linked_list([4, 1, 8, 4, 5]), head_b=create_linked_list([5, 6, 1, 8, 4, 5])))
    # print(sol.run(head_a=create_linked_list([1, 9, 1, 2, 4]), head_b=create_linked_list([3, 2, 4])))
    # FIXME: I failed to reproduce the act of two linked list, so the answer showed in pycharm is wrong (but it is correct in leetcode)
    # e.g.
    #     4 - 1 \
    #             8 - 4 - 5
    # 5 - 6 - 1 /
    # but the code below can't express that behavior
    # head_a = create_linked_list([4, 1, 8, 4, 5])
    # head_b = create_linked_list([5, 6, 1, 8, 4, 5])
