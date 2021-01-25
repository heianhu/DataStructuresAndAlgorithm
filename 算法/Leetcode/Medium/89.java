/**
 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

 格雷编码序列必须以 0 开头。



 示例 1:

 输入: 2
 输出: [0,1,3,2]
 解释:
 00 - 0
 01 - 1
 11 - 3
 10 - 2

 对于给定的 n，其格雷编码序列并不唯一。
 例如，[0,2,3,1] 也是一个有效的格雷编码序列。

 00 - 0
 10 - 2
 11 - 3
 01 - 1
 示例 2:

 输入: 0
 输出: [0]
 解释: 我们定义格雷编码序列必须以 0 开头。
 给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
 因此，当 n = 0 时，其格雷编码序列为 [0]。
 */

import java.util.*;


class Solution {
    /**
     * 0
     *
     * 0 1
     *
     * 00 01  11 10
     *
     * 000 001 011 010  110 111 101 100
     */
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        result.add(0);
        // 记录当前需要加几，每次循环向左移一位
        int bit = 1;
        for (int i = 1; i <= n; i++) {
            int resultSize = result.size();
            // 从右向左加
            for (int j = resultSize - 1; j >= 0; j--) {
                result.add(result.get(j) + bit);
            }
            bit <<= 1;
        }
        return result;
    }
}

