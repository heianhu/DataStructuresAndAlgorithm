#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def creat_link(points: List[int]) -> ListNode:
    link_head = None
    tail = None
    for x in points[::-1]:
        link_head = ListNode(x)
        link_head.next = tail
        tail = link_head
    return link_head


def print_link(link_head):
    point = link_head
    while point:
        print(point.val, end='->')
        point = point.next
    print('\n', '-'*10, sep='')


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp_head1 = l1
        tmp_head2 = l2
        # 建一个空的中间值(不能直接等于l1/l2的第一个值，因为l1/l2有可能为空)
        result_head = ListNode(0)
        tmp_result_point = result_head

        while tmp_head1 and tmp_head2:
            if tmp_head1.val <= tmp_head2.val:
                tmp_result_point.next = ListNode(tmp_head1.val)
                tmp_head1 = tmp_head1.next
            else:
                tmp_result_point.next = ListNode(tmp_head2.val)
                tmp_head2 = tmp_head2.next
            tmp_result_point = tmp_result_point.next

        if tmp_head1:
            tmp_result_point.next = tmp_head1
        else:
            tmp_result_point.next = tmp_head2

        result_head = result_head.next
        return result_head


if __name__ == '__main__':
    link1 = creat_link([1, 2, 4])
    print_link(link1)
    link2 = creat_link([1, 3, 4])
    print_link(link2)
    link = Solution().mergeTwoLists(link1, link2)
    print_link(link)
