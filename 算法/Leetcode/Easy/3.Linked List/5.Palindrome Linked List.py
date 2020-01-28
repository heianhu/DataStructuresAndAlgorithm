#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
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
    @staticmethod
    def find_length_mid(head: ListNode) -> (int, int):
        tmp_head = head
        count = 0
        while tmp_head:
            count += 1
            tmp_head = tmp_head.next
        return count, count//2

    @staticmethod
    def reversed(head: ListNode, reversed_point=0) -> None:
        """
        将需要翻转的节点之后的链表全部翻转
        """
        tmp_head = head
        while reversed_point > 1:
            # 保留一位
            reversed_point -= 1
            tmp_head = tmp_head.next
        reversed_point = tmp_head.next

        pre_point = None
        reversed_head = None
        while reversed_point:
            reversed_head = reversed_point
            reversed_point = reversed_point.next
            reversed_head.next = pre_point
            pre_point = reversed_head
        tmp_head.next = reversed_head

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        tmp_head = head

        length, mid = self.find_length_mid(head)
        self.reversed(tmp_head, mid)
        mid_point = head
        for _ in range(mid):
            mid_point = mid_point.next
        for _ in range(mid):
            if tmp_head.val != mid_point.val:
                tmp_head = head
                self.reversed(tmp_head, mid)
                return False
            else:
                tmp_head = tmp_head.next
                mid_point = mid_point.next
        tmp_head = head
        self.reversed(tmp_head, mid)
        return True


if __name__ == '__main__':
    test = Solution()

    link1 = creat_link(['12', [1, 2], (1, 2), '12'])
    # link1 = creat_link([1, 2, 2, 1])
    print_link(link1)
    print(Solution().isPalindrome(link1))
    print_link(link1)
