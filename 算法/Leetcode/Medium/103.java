/**
 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

 例如：
 给定二叉树 [3,9,20,null,null,15,7],

 3
 / \
 9  20
 /  \
 15   7
 返回锯齿形层序遍历如下：

 [
 [3],
 [20,9],
 [15,7]
 ]
 */

import java.util.*;


class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        if (root == null) {
            return result;
        }
        boolean isOrder = true;
        Queue<TreeNode> treeNodeQueue = new LinkedList<>();
        treeNodeQueue.offer(root);
        while (!treeNodeQueue.isEmpty()) {
            int thisLevelNodeSize = treeNodeQueue.size();
            List<Integer> resultTmp = new LinkedList<>();
            for (int i = 0; i < thisLevelNodeSize; i++) {
                // 从左到右取出上一层的节点
                TreeNode treeNode = treeNodeQueue.poll();
                // 按既定顺序插入到结果中
                if (isOrder) {
                    resultTmp.add(treeNode.val);
                } else {
                    resultTmp.add(0, treeNode.val);
                }
                // 将该节点的子节点从左到右插入到队列中
                if (treeNode.left != null) {
                    treeNodeQueue.offer(treeNode.left);
                }
                if (treeNode.right != null) {
                    treeNodeQueue.offer(treeNode.right);
                }
            }
            result.add(new LinkedList<>(resultTmp));
            // 反转顺序
            isOrder = !isOrder;
        }
        return result;
    }
}

