/**
 给出一个区间的集合，请合并所有重叠的区间。

 示例 1:

 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
 输出: [[1,6],[8,10],[15,18]]
 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
 示例 2:

 输入: intervals = [[1,4],[4,5]]
 输出: [[1,5]]
 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。



 提示：

 intervals[i][0] <= intervals[i][1]
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public int[][] merge(int[][] intervals) {
        int intervalsLength = intervals.length;
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            } else {
                return a[0] - b[0];
            }
        });
        List<int[]> result = new ArrayList<>();
        int[] tmpResult = intervals[0];
        for (int i = 1; i < intervalsLength; i++) {
            if (intervals[i][0] <= tmpResult[1]) {
                tmpResult[1] = Math.max(intervals[i][1], tmpResult[1]);
            } else {
                result.add(tmpResult);
                tmpResult = intervals[i];
            }
        }
        // 插入最后一个值
        result.add(tmpResult);
        int[][] tmp = new int[result.size()][2];
        IntStream.range(0, result.size()).forEach(idx -> tmp[idx] = result.get(idx));
        return tmp;
    }
}

