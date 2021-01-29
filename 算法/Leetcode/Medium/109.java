/**
 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

 示例:

 给定的有序链表： [-10, -3, 0, 5, 9],

 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

 0
 / \
 -3   9
 /   /
 -10  5
 */

import java.util.*;


class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }
        List<Integer> listNodeArray = new ArrayList<>();
        while (head != null) {
            listNodeArray.add(head.val);
            head = head.next;
        }
        return buildTreeNode(listNodeArray, 0, listNodeArray.size() - 1);
    }

    TreeNode buildTreeNode(List<Integer> listNodeArray, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = (left + right) / 2;
        TreeNode result = new TreeNode(listNodeArray.get(mid));
        result.left = buildTreeNode(listNodeArray, left, mid - 1);
        result.right = buildTreeNode(listNodeArray, mid + 1, right);
        return result;
    }
}

