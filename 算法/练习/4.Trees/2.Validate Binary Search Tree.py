#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
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
    def __init__(self):
        self.check_list = list()

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        # if root.val is None:
        #     return True
        self.isValidBST(root.left)
        self.check_list.append(root.val)
        self.isValidBST(root.right)

        if self.check_list == sorted(self.check_list) and len(self.check_list) == len(set(self.check_list)):
            return True
        else:
            return False

    # def __del__(self):
    #     print(self.check_list)


if __name__ == '__main__':
    tree = create_tree([2,1,3])
    print(Solution().isValidBST(tree))
    tree = create_tree([5,1,4,null,null,3,6])
    print(Solution().isValidBST(tree))
