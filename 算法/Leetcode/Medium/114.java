/**
 给你二叉树的根结点 root ，请你将它展开为一个单链表：

 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
 展开后的单链表应该与二叉树 先序遍历 顺序相同。


 示例 1：


 输入：root = [1,2,5,3,4,null,6]
 输出：[1,null,2,null,3,null,4,null,5,null,6]
 示例 2：

 输入：root = []
 输出：[]
 示例 3：

 输入：root = [0]
 输出：[0]


 提示：

 树中结点数在范围 [0, 2000] 内
 -100 <= Node.val <= 100


 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
 */

import java.util.*;


class Solution {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        TreeNode leftRoot = root.left;
        TreeNode rightRoot = root.right;

        // 获得调整好的右子树root
        flatten(rightRoot);

        if (leftRoot != null) {
            // 获得调整好的左子树root
            flatten(leftRoot);

            // 让当前的root左子树为null
            root.left = null;

            // 让当前的root右子树为调整好的左子树root
            root.right = leftRoot;

            // 遍历调整好的左子树root到右节点为null，将其右节点设为调整好的右子树root
            while (root.right != null) {
                root = root.right;
            }
            root.right = rightRoot;
        }
    }
}

