#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        tmp = TreeNode(nums[(len(nums) - 1) // 2])
        tmp.left = self.sortedArrayToBST(nums[0:(len(nums) - 1) // 2])
        tmp.right = self.sortedArrayToBST(nums[(len(nums) - 1) // 2 + 1:])
        return tmp


if __name__ == '__main__':
    tree = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print_tree(tree)
