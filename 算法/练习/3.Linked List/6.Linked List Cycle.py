#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

3 -> 2 -> 0 -> -4
     ^          /
     |_________/


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

1 -> 2
^   /
|__/


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

1


Follow up:

Can you solve it using O(1) (i.e. constant) memory?
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        one_step_head = head
        two_step_head = head
        while two_step_head and two_step_head.next:
            one_step_head = one_step_head.next
            two_step_head = two_step_head.next.next
            if one_step_head is two_step_head:
                return True
        return False




