#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
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
    def reverseList(self, head: ListNode) -> ListNode:
        result_head = None
        tail = None
        tmp_head = head
        while tmp_head:
            result_head = ListNode(tmp_head.val)
            result_head.next = tail
            tail = result_head
            tmp_head = tmp_head.next
        return result_head


if __name__ == '__main__':
    link = creat_link([1, 2, 3])
    print_link(link)
    link = Solution().reverseList(link)
    print_link(link)
