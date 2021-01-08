/**
 * 
'[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成
 */

import java.util.*;

class Solution {
    Map<String, List<Node>> stringNodeListMap;
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        double[] result = new double[queries.size()];
        stringNodeListMap = new HashMap<>();
        // 构建所用的图
        for (int i = 0; i < equations.size(); i++) {
            String dividend = equations.get(i).get(0);
            String divisor = equations.get(i).get(1);

            // 如果图中没有节点则初始化节点
            if (!stringNodeListMap.containsKey(dividend)) {
                stringNodeListMap.put(dividend, new ArrayList<>());
            }
            // 加入该节点对应的邻接节点值
            stringNodeListMap.get(dividend).add(new Node(divisor, values[i]));

            // 对分母做同样操作
            if (!stringNodeListMap.containsKey(divisor)) {
                stringNodeListMap.put(divisor, new ArrayList<>());
            }
            stringNodeListMap.get(divisor).add(new Node(dividend, 1 / values[i]));
        }
        for (int i = 0; i < queries.size(); i++) {
            result[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), 1.0, new HashSet<>());
        }
        return result;
    }

    private double dfs(String current, String target, double result, Set<String> hasDone) {
        if (hasDone.contains(current) || !stringNodeListMap.containsKey(current)) {
            return -1.0;
        }
        if (current.equals(target)) {
            return result;
        }
        
        hasDone.add(current);
        for (Node node:stringNodeListMap.get(current)) {
            // 继续dfs，倍数需要乘上下个一个节点的倍数
            double temp = dfs(node.point, target, result * node.num, hasDone);
            if (temp != -1.0) {
                // 如果搜到了答案，就直接返回答案
                return temp;
            }
        }

        return -1.0;
    }
}

/**
 * 邻接节点类，point为邻接节点代表的字符串，num为到达邻接节点所需的倍数
 */
class Node {
    public String point;
    public double num;

    public Node(String point, double num) {
        this.point = point;
        this.num = num;
    }
}
