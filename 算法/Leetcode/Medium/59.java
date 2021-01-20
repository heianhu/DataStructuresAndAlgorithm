/**
 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

 示例:

 输入: 3
 输出:
 [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
 ]
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public int[][] generateMatrix(int n) {
        int[][] result = new int[n][n];
        boolean[][] resultIsUsed = new boolean[n][n];
        int num = 1;
        int usedIndex = 0;
        while (num <= n * n) {
            for (int i = 0; i < n; i++) {
                if (!resultIsUsed[usedIndex][i]) {
                    resultIsUsed[usedIndex][i] = true;
                    result[usedIndex][i] = num++;
                }
            }
            for (int i = 0; i < n; i++) {
                if (!resultIsUsed[i][n - usedIndex - 1]) {
                    resultIsUsed[i][n - usedIndex - 1] = true;
                    result[i][n - usedIndex - 1] = num++;
                }
            }
            for (int i = n - 1; i >= 0; i--) {
                if (!resultIsUsed[n - usedIndex - 1][i]) {
                    resultIsUsed[n - usedIndex - 1][i] = true;
                    result[n - usedIndex - 1][i] = num++;
                }
            }
            for (int i = n - 1; i >= 0; i--) {
                if (!resultIsUsed[i][usedIndex]) {
                    resultIsUsed[i][usedIndex] = true;
                    result[i][usedIndex] = num++;
                }
            }
            usedIndex++;
        }
        return result;
    }
}
