/**
 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

 说明: 叶子节点是指没有子节点的节点。

 示例:
 给定如下二叉树，以及目标和 sum = 22，

 5
 / \
 4   8
 /   / \
 11  13  4
 /  \    / \
 7    2  5   1
 返回:

 [
 [5,4,11,2],
 [5,8,4,5]
 ]
 */

import java.util.*;


class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        dfs(root, result, targetSum, new Stack<>());
        return result;
    }

    void dfs(TreeNode root, List<List<Integer>> result, int target, Stack<Integer> tmpStack) {
        if (root == null) {
            return;
        }
        if (isRoot(root)) {
            if (target == root.val) {
                tmpStack.push(root.val);
                result.add(new ArrayList<>(tmpStack));
                tmpStack.pop();
            }
            return;
        }
        tmpStack.push(root.val);
        target -= root.val;
        dfs(root.left, result, target, tmpStack);
        dfs(root.right, result, target, tmpStack);
        tmpStack.pop();
    }

    boolean isRoot(TreeNode treeNode) {
        return treeNode != null && treeNode.left == null && treeNode.right == null;
    }
}

