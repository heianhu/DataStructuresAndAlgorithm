#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List
from queue import Queue

null = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(head: TreeNode):
    if head:
        print(head.val)
        print_tree(head.left)
        print_tree(head.right)


def create_tree(point: List[int], index=0) -> TreeNode or None:
    if len(point) <= index:
        return None
    if point[index] is None:
        return
    current_node = TreeNode(point[index])
    current_node.left = create_tree(point, 2 * index + 1)
    current_node.right = create_tree(point, 2 * index + 2)

    return current_node


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level_order_list = list()
        node_list = list()
        node_list.append(root)
        while node_list:
            level_order_list.append(
                [
                    node.val
                    for node in node_list
                ]
            )
            node_list = [
                j
                for i in [(node.left, node.right) for node in node_list]
                for j in i
                if j is not None
            ]
        return level_order_list


if __name__ == '__main__':
    tree = create_tree([4, 2, 6, 1, 3, 5, 7])
    print(Solution().levelOrder(tree))
    # tree = create_tree([1, 2, 2, null, 3, null, 3])
    # print(Solution().levelOrder(tree))
    # tree = create_tree([3, 9, 20, null, null, 15, 7])
    # print(Solution().levelOrder(tree))
