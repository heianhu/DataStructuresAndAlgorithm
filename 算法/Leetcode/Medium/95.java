/**
 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。



 示例：

 输入：3
 输出：
 [
 [1,null,3,2],
 [3,2,null,1],
 [3,1,null,null,2],
 [2,1,3],
 [1,null,2,null,3]
 ]
 解释：
 以上的输出对应以下 5 种不同结构的二叉搜索树：

 1

  1    2
  \    /
  2   1


 1         3     3      2      1
 \       /     /      / \      \
 3     2     1      1   3      2
 /     /       \                 \
 2     1         2                 3


 提示：

 0 <= n <= 8
 */

import java.util.*;


class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return new ArrayList<>();
        }
        return dfs(1, n);
    }

    List<TreeNode> dfs(int start, int end) {
        List<TreeNode> result = new ArrayList<>();
        if (start > end) {
            result.add(null);
            return result;
        }

        for (int i = start; i <= end; i++) {
            List<TreeNode> leftTrees = dfs(start, i - 1);
            List<TreeNode> rightTrees = dfs(i + 1, end);

            for (TreeNode left : leftTrees) {
                for (TreeNode right : rightTrees) {
                    TreeNode cur = new TreeNode(i, left, right);
                    result.add(cur);
                }
            }
        }
        return result;
    }
}

