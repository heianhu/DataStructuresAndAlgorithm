#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
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

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_queue = list()
        right_queue = list()
        left_queue.append(root.left)
        right_queue.append(root.right)
        while left_queue and right_queue:
            left = left_queue.pop(0)
            right = right_queue.pop(0)
            if left is None and right is None:
                continue
            if (left is None and right is not None) or (left is not None and right is None):
                return False
            if left.val != right.val:
                return False
            left_queue.extend([left.right, left.left])
            right_queue.extend([right.left, right.right])
        return True

    # def __init__(self):
    #     self.check_list = list()
    #
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     """
    #     通过中序遍历查看list是否对称
    #     因为构造树的情况不同，如果过滤掉null的情况，会出现不同的结果
    #     """
    #     if not root:
    #         return True
    #     self.isSymmetric(root.left)
    #     self.check_list.append(root.val)
    #     self.isSymmetric(root.right)
    #
    #     print(self.check_list)
    #     if len(self.check_list) % 2:
    #         if self.check_list[:len(self.check_list) // 2] == self.check_list[len(self.check_list) // 2 + 1:][::-1]:
    #             return True
    #         else:
    #             return False
    #     else:
    #         if self.check_list[:len(self.check_list) // 2] == self.check_list[len(self.check_list) // 2:][::-1]:
    #             return True
    #         else:
    #             return False


if __name__ == '__main__':
    tree = create_tree([1, 2, 2, 3, 4, 4, 3])
    print(Solution().isSymmetric(tree))
    tree = create_tree([1, 2, 2, null, 3, null, 3])
    print(Solution().isSymmetric(tree))
    tree = create_tree([1, 2, 2, 2, null, 2])
    print(Solution().isSymmetric(tree))
