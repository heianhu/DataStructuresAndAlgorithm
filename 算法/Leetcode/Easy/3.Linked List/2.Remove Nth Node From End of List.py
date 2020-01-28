#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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
        print(point.val)
        point = point.next
    print('-'*10)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current_point = head
        pre_point = None

        count = 1
        while current_point.next:
            count += 1
            pre_point = current_point
            current_point = current_point.next
        if n == count:
            # 删除第一个
            head = head.next
        elif n == 1:
            # 删除最后一个
            pre_point.next = None
        else:
            current_point = head
            while count - n > 1:
                current_point = current_point.next
                count -= 1
            # print(current_point.val)
            current_point.next = current_point.next.next

        return head


if __name__ == '__main__':
    link = creat_link([1, 2, 3])
    print_link(link)
    link = Solution().removeNthFromEnd(link, 1)
    print_link(link)
