#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
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
    current_node = TreeNode(point[index])
    current_node.left = create_tree(point, 2 * index + 1)
    current_node.right = create_tree(point, 2 * index + 2)

    return current_node


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    tree = create_tree([3,9,20,null,null,15,7])
    # print_tree(tree)
    print(Solution().maxDepth(tree))
