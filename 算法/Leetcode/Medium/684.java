/**
 在本问题中, 树指的是一个连通且无环的无向图。

 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

 示例 1：

 输入: [[1,2], [1,3], [2,3]]
 输出: [2,3]
 解释: 给定的无向图为:
 1
 / \
 2 - 3
 示例 2：

 输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
 输出: [1,4]
 解释: 给定的无向图为:
 5 - 1 - 2
 |   |
 4 - 3
 注意:

 输入的二维数组大小在 3 到 1000。
 二维数组中的整数在1到N之间，其中N是输入数组的大小。
 */

import java.util.*;



class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        // 初始化树
        int[] tree = new int[edges.length + 1];
        int[] rank = new int[edges.length + 1];
        Arrays.fill(tree, -1);
        Arrays.fill(rank, 0);

        for (int[] points:edges) {
            int x = points[0];
            int y = points[1];
            if (!union(x, y, tree, rank)) {
                return new int[] {x, y};
            }
        }
        return new int[] {-1, -1};
    }

    boolean union(int pointA, int pointB, int[] tree, int[] rank) {
        int pointARoot = find(pointA, tree);
        int pointBRoot = find(pointB, tree);
        if (pointARoot == pointBRoot) {
            return false;
        } else {
            if (rank[pointARoot] < rank[pointBRoot]) {
                // A的高度小于B，将A插入B
                tree[pointARoot] = pointBRoot;
            } else if (rank[pointARoot] > rank[pointBRoot]) {
                // B的高度小于A，将B插入A
                tree[pointBRoot] = pointARoot;
            } else {
                // 高度相同，随便插入一个，将其高度加一
                // 将A插入B
                tree[pointARoot] = pointBRoot;
                // 将B高度加一
                rank[pointBRoot] += 1;
            }
            return true;
        }
    }

    int find(int point, int[] tree) {
        int result = point;
        while (tree[result] != -1) {
            result = tree[result];
        }
        return result;
    }
}

